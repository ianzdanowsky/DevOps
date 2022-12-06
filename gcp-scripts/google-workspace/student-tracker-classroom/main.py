# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly',
          'https://www.googleapis.com/auth/classroom.coursework.me',
          'https://www.googleapis.com/auth/classroom.coursework.me.readonly',
          'https://www.googleapis.com/auth/classroom.coursework.students'
]

SERVICE_ACCOUNT_FILE = '/home/ian/classroom-api/service-account.json'

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
delegated_credentials = creds.with_subject('ian@gsaladeaula.com.br')


def main():

    try:
        service = build('classroom', 'v1', credentials=delegated_credentials)

        # Call the Classroom API
        results = service.courses().list(pageSize=10).execute()
        courses = results.get('courses', [])

        if not courses:
            print('No courses found.')
            return
        # Prints the names of the first 10 courses.
        print('Courses:')
        for course in courses:
            print(course['name'])

    except HttpError as error:
        print('An error occurred: %s' % error)



def get_all_classes_id():
    allClassId = []
    try:
        service = build('classroom', 'v1', credentials=delegated_credentials)

        # Call the Classroom API
        results = service.courses().list().execute()
        courses = results.get('courses', [])

        if not courses:
            print('No courses found.')
            return
        # Prints the names of the first 10 courses.
        for course in courses:
            # print(course['id'])
            allClassId.append(course['id'])

    except HttpError as error:
        print('An error occurred: %s' % error)

    return allClassId




def list_course_work():
    classesId = get_all_classes_id()
    allCourseWork = []
    
    for id in classesId:
        try:
            service = build('classroom', 'v1', credentials=delegated_credentials)

            # Call the Classroom API
            coursework = service.courses().courseWork()
            results = coursework.list(courseId=id).execute()
            courseWorkDict = results.get('courseWork')

            if not courseWorkDict:
                continue
            # Prints the names of the first 10 courses.
            for coursework in courseWorkDict:
                # print(coursework['id'])
                allCourseWork.append(coursework['id'])

        except HttpError as error:
            print('An error occurred: %s' % error)

    return allCourseWork







if __name__ == '__main__':
    list_course_work()