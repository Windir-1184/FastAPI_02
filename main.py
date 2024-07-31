from fastapi import FastAPI
from models import Curso

app = FastAPI()
@app.get('/')
async def root():
    return {"hello": "world"}

@app.get('/infinity')
async def infinity():
    return {'infinity': "school"}

@app.get('/meusdados')
async def meusdados():
    return {"nome": "pacceli", "idade": 35 , "prof": "dev"}

cursos = [
    {"codigo": 1, "nome": "python", "cargaHoraria": 100, "disponivel": True, "notaCorte": 7.5},
    {"codigo": 2, "nome": "JavaScript", "cargaHoraria": 100, "disponivel": False, "notaCorte": 6}
]

@app.get('/cursos')
async def getCursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def getCursoById(curso_id: int):
    for curso in cursos:
        if curso['codigo'] == curso_id:
            return curso
    return{"erro": "curso não encontrado"}

@app.get('/cursos-by-nota')
async def getCursoByNota(nota: float):
    resultado = []
    for curso in cursos:
        if cursos['notaCorte'] >= nota:
            resultado.append(curso)
    return resultado        

@app.post('/cursos')
async def addCurso(curso: Curso):
    cursos.append(curso)
    return {"success": "ok"}

@app.put('/cursos/{curso_id}')
async def editCurso(curso_id: int, curso: Curso):
    for c in cursos:
        if c['codigo'] == curso_id:
            c['nome'] = curso.nome
            c['cargaHoraria'] = curso.cargaHoraria
            c['notaCorte'] = curso.notaCorte
            c['disponivel'] = curso.disponivel
            return c
    return {"erro": "curso não encontrado"} 


@app.delete('/cursos/{curso_id}')
async def deleteCurso(curso_id: int):
    for curso in cursos:
        if curso['codigo'] == curso_id:
            cursos.remove(curso)
            return {"successs": "ok"}
    return {"erro": "true"}    


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', reload=True, port=8000)