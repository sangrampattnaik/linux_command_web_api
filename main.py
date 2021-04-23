from fastapi import FastAPI,HTTPException
import uvicorn
import subprocess as sp

app = FastAPI()

@app.get("/")
def home(command:str = 'echo "hello world"'):
    '''
    Executes a linux command and returns the result.
    params:
        command (Query Paramaeter in request) : linux shell command
    '''
    command_out = sp.run(command,shell=True,capture_output=True)
    if command_out.returncode == 0:
        response = command_out.stdout
    else:
        raise HTTPException(status_code=400, detail=f"{command} command not found")
    return {"status":"success","data":response}

if __name__ == "__main__":
    uvicorn.run(app=app,debug=True,port=7000) # run server on http://127.0.0.1:7000