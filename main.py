## pip install fastapi uvicorn
#
from fastapi import FastAPI, Request
import uvicorn
from typing import Union
import pandas as pd

app = FastAPI()
sapid=[]
@app.get("/sapid/{item_id}")
def read_root(item_id:int,q=Union[str,None]=None):
    sapid.append(item_id)
    print(f"\n{sapid}\n")
    data={"present":sapid}
    df=pd.DataFrame(data)
    df.to_excel("3_idiotAttendance.xlsx")

    return {"Attendance Marked":item_id}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

