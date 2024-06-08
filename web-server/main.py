import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


#instancia 1 app
app=FastAPI()


#END POINTS
@app.get('/')
def get_list():
    return[1,2,3]

@app.get('/contact', response_class=HTMLResponse )
def get_list():
    return"""
        <h2>Hola soy una pagina</h2>
        <p>primera linea de parrafo<br><strong>LINEA NEGRA</strong></p>
        <button><em>OPRIMEME</em></button>
    """

def run():
    store.get_categories()

if __name__=='__main__':
    run()
    