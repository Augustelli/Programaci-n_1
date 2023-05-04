from flask import request, abort, jsonify
from .. import db
from main.models import ClasesModelo
from flask_restful import Resource


class Clases_R(Resource):

    def get(self):
        try:
            clases = db.session.query(ClasesModelo)
            page=1
            per_page=10
            if request.args.get('page'):
                page = int(request.args.get('page'))
            if request.args.get('per_page'):
                per_page = int(request.args.get('per_page'))
            clases1 = clases.paginate(page=page, per_page=per_page, error_out=False, max_per_page=30) 
            clases_lista = list()
            for clase in clases:
                clase_dict = {}
                clase_dict['idClases'] = clase.idClases
                clase_dict['nombre'] = clase.nombre
                clase_dict['dias'] = clase.dias
                clases_lista.append(clase_dict)
            
            return jsonify({'Clases':clases_lista,
                           'Pagina':page,
                            'Por pagina':per_page,
                            'Total':clases1.total
                            })
        except BaseException:
            abort(404, 'No se ha encontrado la Clase')
        finally:
            db.session.close()


       
        
    def post(self):
        try:
            clase_nueva= ClasesModelo.from_json(request.get_json())
            db.session.add(clase_nueva)
            db.session.commit()
            return clase_nueva.to_json(), 201
        except BaseException:
            abort(404, 'Error al crear la clase')
        finally:
            db.session.close()


# 



class Clase_R(Resource):

    def delete(self, user_id):
        try:
            clase_eliminar = db.session.query(ClasesModelo).filter(
                ClasesModelo.idClases == user_id).first()
            db.session.delete(clase_eliminar)
            db.session.commit()
            return 204
    


        except BaseException:
            abort(404, 'No se ha encontrado la clase {}'.format(user_id))
        finally:
            db.session.close()

        
    
    def get(self,user_id):
        try:
            clase= db.session.query(ClasesModelo).filter(
                   ClasesModelo.idClases == user_id).first()
            return clase.to_json(), 201
        except BaseException:
            abort(404, 'No se ha encontrado la Clase')
        finally:
            db.session.close()




    def put(self, user_id):
        try:
            clase_modificar = db.session.query(ClasesModelo).filter(
                ClasesModelo.idClases == user_id).first()
            informacion = request.get_json().items()
            for campo, valor in informacion:
                setattr(clase_modificar, campo, valor)
            db.session.add(clase_modificar)
            db.session.commit()

            return clase_modificar.to_json(), 201
        except BaseException:
            abort(404, 'No se ha encontrado la Clase')
        finally:
            db.session.close()



