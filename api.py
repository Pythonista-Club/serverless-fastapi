from fastapi import FastAPI
from mangum import Mangum


api = FastAPI()
handler = Mangum(api)


@api.get("/")
def get_root():
    """_summary_
    Baseline method of the application
    """
    return {"resp":"Welcome Lambda, to the Pythonista Club! "}
