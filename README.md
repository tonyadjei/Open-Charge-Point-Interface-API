# Open-Charge-Point-Interface-API
A FastAPI RESTful  implementation of the sessions module in OCPI (Open Charge Point Interface) for communication b/n EV drivers and Charge Point Operators.

## Packages/tools required:

    pip3 install fastapi "uvicorn[standard]" (linux)
    or
    pip install fastapi "uvicorn[standard]" (windows)



## Running the servers:

   - For the Sender Interface, after extracting the project, navigate to the Sender folder > main.py > then run "python main.py" or "python3 main.py"
   - For the Receiver Interface, after extracting the project, navigate to the Receiver folder > main.py > then run "python main.py" or "python3 main.py"
   - Open the browser and type <127.0.0.1:8000/docs> to interact with the Sender Interface or <127.0.0.1:9000/docs> to interact with the Receiver Interface.



## Notes/Additional information:

   - For the sake of creating a simple reply/request API, there is no connected database. As a result, the data is not persistent. However, if the server is not reloaded, the data in memory will persist.

   - Use localhost:8000/docs to access the interactive documentation or localhost:8000/redoc for a static non-interactive documentation.

   - The Sender Interface is set to run on port=8000 whereas the Receiver Interface is set to run on port=9000

   - Data about session objects needed for performing requests(query parameters, path/route parameters etc.) can be found in the <data.py> file of each Interface folder.

   - For purposes of simplicity, id fields of session objects in the Receiver Interface have been set.

   - Data types of object fields were not strictly followed for simplicity's sake and time constraints.
