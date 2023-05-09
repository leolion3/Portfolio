#!/usr/bin/env python3
import requests
from getpass import getpass

class StudIPAuthenticator():

    def __init__(self):
        self.BASE_URL = 'https://elearning.uni-bremen.de/index.php'
        self.LOGIN_URL = f'{self.BASE_URL}?again=yes'
        self.seminar_session = ''

    def authenticate(self, username: str, password: str) -> requests.Session:
        data = {
            'loginname' : username,
            'password' : password
        }

        s = requests.Session()
        r = requests.get(self.LOGIN_URL)

        self.security_token = r.text.split('name="security_token" value="')[1].split('"')[0]
        login_ticket = r.text.split('name="login_ticket" value="')[1].split('"')[0]
        resolution = '1920x1080'
        device_pixel_ratio = 1

        data['security_token'] = self.security_token
        data['login_ticket'] = login_ticket
        data['resolution'] = resolution
        data['device_pixel_ratio'] = 1
        data['login'] = ''

        self.seminar_session = dict(r.cookies)['Seminar_Session']

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': f'Seminar_Session={self.seminar_session};',
            'Host': 'elearning.uni-bremen.de',
            'Origin': 'https://elearning.uni-bremen.de',
            'Referer': 'https://elearning.uni-bremen.de/index.php?again=yes',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

        r = s.post(self.LOGIN_URL, headers=headers, data=data)
        return s

    def apply_for_course(self, session: requests.Session, course_id: str):
        url = f'https://elearning.uni-bremen.de/dispatch.php/course/enrolment/apply/{course_id}?apply=1'
        r = session.get(url, cookies=session.cookies)
        csrf_token = r.text.split('CSRF_TOKEN: {')[1].split('value: \'')[1].split('\'')[0]
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,de;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'elearning.uni-bremen.de',
            'Origin': 'https://elearning.uni-bremen.de',
            'Referer': f'https://elearning.uni-bremen.de/dispatch.php/course/details?sem_id={course_id}',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
        data = {
            'security_token' : csrf_token,
            'apply' : '1',
            'yes' : ''
        }
        r = session.post(url, headers=headers, data=data, cookies=session.cookies)
        return r.status_code