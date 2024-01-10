<div align='center'>

<h1>API Blog</h1>
<p>It is an API for blog that uses various themes and libraries This project can help you have a better understanding of design patterns, API writing, load testing, unit testing, background process, etc., and you can help me in further development and optimization.</p>

<h4> <span> · </span> <a href="https://github.com/Mohammad222PR/advance-blog/blob/master/README.md"> Documentation </a> <span> · </span> <a href="https://github.com/Mohammad222PR/advance-blog/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/Mohammad222PR/advance-blog/issues"> Request Feature </a> </h4>


</div>

# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
- [FAQ](#grey_question-faq)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)


## :star2: About the Project
### :space_invader: Tech Stack
<details> <summary>Client</summary> <ul>
<li><a href="">Django</a></li>
<li><a href="">Python</a></li>
<li><a href="">DRF</a></li>
</ul> </details>
<details> <summary>Database</summary> <ul>
<li><a href="">sql3</a></li>
</ul> </details>
<details> <summary>DevOps</summary> <ul>
<li><a href="">docker</a></li>
<li><a href="">Nginx</a></li>
<li><a href="">gunicorn</a></li>
<li><a href="">CI with github actions</a></li>
</ul> </details>

### :dart: Features
- load testing
- background process
- jwt auth
- djoser
- fake object
- caching
- ready for deploy
- CI


### :art: Color Reference
| Color | Hex |
| --------------- | ---------------------------------------------------------------- |
| Primary Color | ![#2f69c6](https://via.placeholder.com/10/2f69c6?text=+) #2f69c6 |
| Secondary Color | ![#393E46](https://via.placeholder.com/10/393E46?text=+) #393E46 |
| Accent Color | ![#00ADB5](https://via.placeholder.com/10/00ADB5?text=+) #00ADB5 |
| Text Color | ![#EEEEEE](https://via.placeholder.com/10/EEEEEE?text=+) #EEEEEE |

## :toolbox: Getting Started

### :bangbang: Prerequisites

- install docker in your computer <a href="https://www.bing.com/ck/a?!&&p=4958b8d70fe4c5c6JmltdHM9MTcwNDg0NDgwMCZpZ3VpZD0zNWFiOGNkZC0xNTdjLTY0ZWQtMWFhNy05ZTAzMTRhZTY1YzcmaW5zaWQ9NTE2Ng&ptn=3&ver=2&hsh=3&fclid=35ab8cdd-157c-64ed-1aa7-9e0314ae65c7&psq=docker+install&u=a1aHR0cHM6Ly9kb2NzLmRvY2tlci5jb20vZW5naW5lL2luc3RhbGwv&ntb=1"> Here</a>
- install python on your computer<a href="https://www.bing.com/ck/a?!&&p=8763eef1e7a29f10JmltdHM9MTcwNDg0NDgwMCZpZ3VpZD0zNWFiOGNkZC0xNTdjLTY0ZWQtMWFhNy05ZTAzMTRhZTY1YzcmaW5zaWQ9NTE3MQ&ptn=3&ver=2&hsh=3&fclid=35ab8cdd-157c-64ed-1aa7-9e0314ae65c7&psq=install+python&u=a1aHR0cHM6Ly93d3cucHl0aG9uLm9yZy9kb3dubG9hZHMv&ntb=1"> Here</a>


### :gear: Installation

setup project
```bash
docker-compose up
```


### :test_tube: Running Tests

test with testcase
```bash
docker-compose exec backend sh -c "python manage.py test"
```
test with pytest
```bash
docker-compose exec backend sh -c "pytest ."
```
reformat with black
```bash
docker-compose exec backend sh -c "black ."
```
test format with flake8
```bash
docker-compose exec backend sh -c "flake8 ."
```


### :running: Run Locally

Clone the project

```bash
https://github.com/Mohammad222PR/advance-blog.git
```
run project in local
```bash
docker-compose exec backend sh -c "python manage.py runserver"
```


## :wave: Contributing

<a href="https://github.com/Mohammad222PR/advance-blog.git/graphs/contributors"> <img src="https://contrib.rocks/image?repo=Louis3797/awesome-readme-template" /> </a>

Contributions are always welcome!

see `contributing.md` for ways to get started

### :scroll: Code of Conduct

Please read the [Code of Conduct](https://github.com/Mohammad222PR/advance-blog.git/blob/master/CODE_OF_CONDUCT.md)

## :grey_question: FAQ

- What should we do if we get into trouble?
- create the issues
- Can we add a new option?
- Yes, you just need to send me your changes with pull request, it will be checked after checking


## :warning: License

Distributed under the no License. See LICENSE.txt for more information.

## :handshake: Contact

mohammadhossein eslami - [@linkdin](https://www.linkedin.com/in/mohammad--eslami) - mohammades13851@gmail.com

Project Link: [https://github.com/Mohammad222PR/advance-blog.git](https://github.com/Mohammad222PR/advance-blog.git)

## :gem: Acknowledgements

Use this section to mention useful resources and libraries that you have used in your projects.

- [pytest](https://docs.pytest.org/en/7.4.x/)
- [jwt](https://jwt.io/)
- [Redis]()
- [celery]()
- [locust]()
- [black]()
- [Faker]()
- [django-celery-beat]()
- [flake8]()
- [drf-yasg]()
- [django-filter]()
- [django-cleanup]()
- [djangorestframework]()
