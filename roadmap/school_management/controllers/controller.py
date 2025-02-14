import json
from odoo import http
from odoo.http import request

class getStudentList(http.Controller):
    @http.route("/api/students", methods=["GET"], type='http', auth='none', csrf=False)
    def getJsonData(self):
        students = request.env['sm.student'].sudo().search([])
        students_data = [
            {
                'id': student.id,
                'name': student.name,
                'age': student.age,
                'school': student.school_name,
                'class': student.class_list
            }
            for student in students
        ]
        return request.make_response(
            json.dumps(students_data),
            headers={'Content-Type': 'application/json'}
        )
        
class createStudent(http.Controller):
    @http.route('/api/student',methods=["POST"], type='http', auth='none', csrf=False)
    def createStudent(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env['sm.student'].sudo().create({
            "name": vals["name"],
            "age": vals["age"],
            "class_ids": [(6, 0, vals["class_ids"])]
        })
        # res = request.env['sm.student'].sudo().create(vals)
        if res:
            return request.make_json_response({
                "message": "Student has been created"
            }, status=200)