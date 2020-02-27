import datetime

from docxtpl import DocxTemplate

now = datetime.datetime.now()
doc = DocxTemplate("template.docx")
context = {'company': "CompanyName",
           'emploer_name': "ФИО_0",
           'type': "Акт приема-передачи оборудования",
           'doc_name': "доверенности №123456",
           'emploee_name': "ФИО_1",
           'doc_initials': "Инициалы_0",
           'emp_initials': "Инициалы_1",
           'date': now}
name, time, = context['emploee_name'], context['date'],
header = f'{name}-{time}'
doc.render(context)
doc.save(header + '.docx')
