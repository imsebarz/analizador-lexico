from myLanguage.repl import start_repl
import uvicorn

def main() -> None:
    print('Bienvenido al analizador léxico de Sebas c:')
    print('Escribe una oración para comenzar: ')
    uvicorn.run("server.api:app", host='0.0.0.0', port=8000, reload=True)


if __name__ == '__main__':
    main()
