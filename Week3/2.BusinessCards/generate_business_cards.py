import json


def generate_head(name):
    return '''<head>
<title>{}</title>
<link rel=stylesheet type=text/css href="styles.css">
</head>'''.format(name)


def generate_body(fullname, avatar_source, age, date,
                  place, gender, interests, skills):
    return '''<body>
<div class="business-card male">
<h1 class="full-name">{}</h1>
<img class="avatar" src="{}">
<div class="base-info">
{}
</div>
<div class="interests">
{}
</div>
<div class="skills">
{}
</div>
</div>
</body>'''.format(fullname, avatar_source,
                  generate_base_info(age, date, place, gender),
                  generate_interests(interests),
                  generate_skills(skills))


def generate_base_info(age, birthdate, birthplace, gender):
    return '''<p>Age: {}</p>
<p>Birth date: {}</p>
<p>Birth place: {}</p>
<p>Gender: {}</p>'''.format(age, birthdate, birthplace, gender)


def generate_content_list(list_of_smth):
    content = []
    for item in list_of_smth:
        content.append("<li>{}</li>".format(item))

    return "\n".join(content)


def generate_interests(interests):
    return '''<h2>Interests:</h2>
<ul>
{}
</ul>'''.format(generate_content_list(interests))


def generate_skills(skills):
    return '''<h2>Skills:</h2>
<ul>
{}
</ul>'''.format(generate_content_list(skills))


def generate_business_card(fullname, avatar_source, age, date,
                           place, gender, interests, skills):
    return '''<!DOCTYPE html>
<html>
{}
{}
</html>'''.format(generate_head(fullname),
                  generate_body(fullname, avatar_source,
                                age, date, place, gender, interests, skills))


def main():
    with open('data.json', 'r') as f:
        data = json.load(f)

    for human in data['people']:
        fullname = "{} {}".format(human['first_name'], human['last_name'])
        avatar_source = "avatars/{}".format(human['avatar'])
        skills = ["{} - {}".format(skill['name'],
                                   skill['level']) for skill in human['skills']]

        html_content = generate_business_card(fullname,
                                              avatar_source,
                                              human['age'],
                                              human['birth_date'],
                                              human['birth_place'],
                                              human['gender'],
                                              human['interests'],
                                              skills)

        with open("{}.html".format(human['first_name'].lower()), 'w') as f:
            f.write(html_content)

if __name__ == '__main__':
    main()
