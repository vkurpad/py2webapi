A simple Dockerized deployemnt of a machine learning model from an IPython notebook to serve up a <a href="https://docs.microsoft.com/en-us/azure/search/cognitive-search-create-custom-skill-example">Custom Web API</a> skill.

Steps to get to a clean build:
<ol>
 <li>Export your model as a pickle file and save it in the <a href="web/outputs">outputs</a> folder</li>
 <li>Update the environment.yml file to add any dependencies and or packages</li>
 <li>Update the <a href="web/project/__init__.py">__init__.py</a> in the project folder to import all the modules needed</li>
 <li>Update the <a href="web/project/__init__.py">__init__.py</a> in the project folder to load the model you saved in the outputs</li>
 <li>If you renamed the env in the environment.yml file, update the <a href="web/Dockerfile">Dockerfile</a> in the web folder to use the new env name. Also update the <a href="docker-compose.yml">docker-compose.yml</a> file with the valid path to gunicorn</li>
 </ol>
 
To build the solution make sure you have docker-compose installed. Run the following command:

<em>docker-compose build</em>

To run the solution run the following command:

<em>docker-compose up</em>

If you are depolying on an Azure VM, remeber to open port 80 to inbound traffic

 
