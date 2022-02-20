from myLanguage.repl import start_repl
import uvicorn

def main() -> None:
    uvicorn.run("server.api:app", host='0.0.0.0', port=8000, reload=True)
    start_repl()


if __name__ == '__main__':
    main()

