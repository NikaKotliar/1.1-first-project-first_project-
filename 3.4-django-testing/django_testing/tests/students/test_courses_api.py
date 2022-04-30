import pytest as pytest
from django.urls import reverse
from rest_framework.test import APIClient
from model_bakery import baker
from random import randint
from students.models import Course, Student

COURSE_URL = '/api/v1/courses/'


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


# проверка получения 1го курса (retrieve-логика)
@pytest.mark.django_db
def test_get_1_course_id_from_path(client, course_factory, student_factory):
    range = 10
    random_int = randint(1, range)
    students = student_factory(_quantity=range)
    courses = course_factory(_quantity=range)

    for i, course in enumerate(courses):
        for i, student in enumerate(students):
            course.students.add(student)

    url = '/api/v1/courses/' + str(random_int) + '/'
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == courses[random_int-1].name

# проверка получения списка курсов (list-логика)
@pytest.mark.django_db
def test_get_courses(client, course_factory, student_factory):
    students = student_factory(_quantity=10)
    courses = course_factory(_quantity=10)

    for i, course in enumerate(courses):
        for i, student in enumerate(students):
            course.students.add(student)

    response = client.get(COURSE_URL)

    data = response.json()
    assert response.status_code == 200

    for i, course in enumerate(data):
        assert course['name'] == courses[i].name

    assert len(data) == len(courses)


# проверка фильтрации списка курсов по id
# создаем курсы через фабрику, передать id одного курса в фильтр, проверить результат запроса с фильтром
@pytest.mark.django_db
def test_get_1_course_by_id_from_query_params(client, course_factory, student_factory):
    range = 15
    random_int = randint(1, range)
    target_course = int(random_int - 1)
    students = student_factory(_quantity=range)
    courses = course_factory(_quantity=range)

    for i, course in enumerate(courses):
        for i, student in enumerate(students):
            course.students.add(student)

    url = '/api/v1/courses/' + '?id=' + str(courses[target_course].id)
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == courses[target_course].id

    # students = student_factory(_quantity=3)
    # course = course_factory()
    # course.students.add(students[0], students[1], students[2])
    #
    # response = client.get(COURSE_URL)
    # data = response.json()
    # assert response.status_code == 200
    # assert data[0]['name'] == course.name
    # assert len(data) == 1


    # проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_get_course_by_name_from_query_params(client, course_factory, student_factory):
    range = 15
    random_int = randint(1, range)
    target_course = int(random_int - 1)
    students = student_factory(_quantity=range)
    courses = course_factory(_quantity=range)

    for i, course in enumerate(courses):
        for i, student in enumerate(students):
            course.students.add(student)

    url = '/api/v1/courses/' + '?name=' + courses[target_course].name
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == courses[target_course].name


# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client, course_factory, student_factory):
    students = student_factory(_quantity=3)
    student_list = [student.id for student in students]
    count = Course.objects.count()
    # assert student_list == 0

    response = client.post(COURSE_URL, data={'name': 'Математика', 'students': student_list})

    assert response.status_code == 201

    assert Course.objects.count() == count + 1

# тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course_factory, student_factory):
    students = student_factory(_quantity=3)
    student_list = [student.id for student in students]
    course = course_factory()
    course.students.add(*student_list)

    url = '/api/v1/courses/' + str(course.id) + '/'
    response = client.patch(url, data={'name': 'русский'})
    response_2 = client.get(url)
    data = response_2.json()
    assert response.status_code == 200
    assert data["name"] == 'русский'

    # тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course_factory, student_factory):
    students = student_factory(_quantity=3)
    student_list = [student.id for student in students]
    course = course_factory()
    course.students.add(*student_list)

    url = '/api/v1/courses/' + str(course.id) + '/'
    response = client.delete(url)
    assert response.status_code == 204

