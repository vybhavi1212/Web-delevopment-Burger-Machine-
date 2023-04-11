<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Vybhavi Chithapuram (vc435)</td></tr>
<tr><td> <em>Generated: </em> 4/11/2023 2:03:19 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/vc435" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231002362-701d7811-25ed-4c5f-bfd3-a0a6395854d0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DIAR-vc435 updated to DIAR-vc435<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231004662-bb6fb779-549c-4306-8f37-b40b3c78ac7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database Tables from VS code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231005446-b058f287-1dd5-42c9-9587-1d69b8dbb716.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code to check if the file is .csv or not<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231005999-05d2d54c-831a-4357-aeea-765c5da144b2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code reading a file and adding text to a dictation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231006285-5640cd61-8f0f-4274-8903-c4228f67fe76.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>In a flash message, the processed record codes are displayed.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231006521-f98f9fb8-d433-4e14-b3c9-4a05a5b051e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code if nothing was loaded<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231066642-4a74546b-e2c4-4e82-84e0-b28f4a7074d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>14records successfully imported<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231066918-77f459f6-5586-4496-9da4-9c759fdf6223.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231067070-82759c2c-36e1-4a24-9901-95059efb4ce0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message when no file is selected.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231014102-4e3b8076-200f-4b37-8dea-e1bc3d72003b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data of employees in table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231014513-33cf5d1b-4663-4711-9e9a-a9a198416d79.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data of companies in table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231012404-7a5695d5-05cd-40ee-bc66-8fd52a0cdb0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Retrieving the first_name, last_name, company (id), email with flash messages if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231012574-875fe501-eb67-496f-b2f7-60ff0a2b4741.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>To print an exception, insert a query and a flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231012961-7cd7ad0f-2faa-4f9a-a06e-b631fceeab0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>message if submitted without being filled .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231013100-a1124a04-f842-473a-820e-536b44fd5f9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231013209-83c29795-540b-47b5-a85e-7dcfbd6426a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message for First_name <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231013387-bcf53c12-b201-416a-8878-df7ba2aa056b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message for Last_name <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231013499-f8732f29-94cd-4a1e-887f-a44c58068898.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231016492-885cea1e-9b9b-4c43-94f0-8b6aa0b7160b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>new employee vybhavi is added<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231018148-30f4ec85-5b10-4d39-978a-5a6eb14c316d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Select query to the retrive data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231018384-d4fcf076-7895-4cae-8e68-c9dc5d245073.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>to check the requested args<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231018544-6206bfbd-83d3-46fc-98bf-3ac8541f260d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Appending like filter for First_name,last_name,email,company_id<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231018974-6149afc7-153e-4a10-8e62-4b3e079aaeb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add the allowable sorting columns.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231019160-8a276bdf-29d4-40b1-b982-6a9317938ca0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message if limit is out of bond<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231019952-a08e5605-f164-48ae-b1ad-8f43232d3902.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Exception handling message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231020468-e264cbc6-41bb-417c-bfb7-2a3c99b81252.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results when first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231020702-ef1ff857-b6cd-4296-87d7-c47eb44a9a47.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results when last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231021133-90d9a616-9b17-4dcc-b593-4178b651067d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results when email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231023590-642d40f8-8eb6-4c64-a1dd-3953afa0cb2d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results when company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231023794-f7423263-da55-481d-8803-890a28d9cce9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results when asc order filter is applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231023919-49503a60-9ded-4530-9b2c-5ff0076bd45a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with desc order filter  is applied<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231024388-6cbc2e4b-e3cf-4d54-a7da-f1b3f0b9c99c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) first_name, last_name, company (id), email from<br>form. Missing id should be handled with a flash message and redirected back<br>to employee search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231024509-ea9b405c-7633-4469-9031-b48be0bf26e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash message first_name, last_name, email, company(not required)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231024619-d82f4e61-efa5-48dc-9fc5-86dd7fefb54c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231024702-ea9efa32-637f-4ae7-aad1-dfef065f705c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except blocks (two) should have a user friendly message flashed and a print()<br>of the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231024784-2f6a14df-122c-42ee-84e9-20ca4bb27b61.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper SELECT query should be visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231024919-b80676e0-900b-4170-a38f-98297220a621.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231025223-77b053dc-7998-491e-862c-cce703c6c955.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before editing shown<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231025314-b573367a-a039-4382-ba32-ac7e5fac9c63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After editing the  data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231026762-6a875445-1c5d-4c24-98e1-5182883cdff9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before editing in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231025652-e638ac49-eeb2-4e9b-932b-c334bab78147.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>editing last name of vybhavi from chithapuram to BILLAPATI and  Company (Feiner<br>bros - Midway Hotel)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231027415-7f4ba427-ba44-48a9-83a8-e938b97c0f3c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieve form data for name, address, city, state, country, zip, website and<br>flash messages if any of them are  missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231028534-31fddf09-2755-41fe-a078-6b126a9a527c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Insert Query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231028793-00307445-a7d9-42ff-8a6b-a0252f7a636a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user-friendly message flashed and a print() of the<br>exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231032231-9bbd3d52-1178-4087-906d-a7159c5c3c46.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Showing filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231034526-561034b1-b07b-4289-be32-0ceec7493a37.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231035876-a21ab9b8-ca1a-45db-bb2b-f4b7b82a0b6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message for company name, address, city, zip code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231036114-e7173dbe-ac67-4c02-b906-643c45a84888.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message if input of state is missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231036306-69f9b678-6672-498c-bfe2-f7e44b54ad54.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message, if input for country is missing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231039840-f670a26d-533f-4a79-b34a-c0c142a360f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should include the valid company data shown previously (Lilly ,  id=45)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231041095-b07d315a-926b-410d-935a-72f815114f9b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Caption: SELECT query should fetch id, name, address, city, country, state, zip, website,<br>employee count (as employee) for the company (likely a sub-query is needed)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231041274-c352dc5b-4697-4852-93c3-3d22435cb194.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Checking for requested args for name, country, state, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231041434-bee8d9dd-4eb5-4f42-8bd7-5ca2cc4976e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append an equality filter for state if provided,if country provided and name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231042043-6221a7fb-3411-4342-bea8-8fed4ebd66d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append sorting if column and order are provided and within the allows columsn<br>and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231043710-fd757184-6947-45c9-9d5f-bb99f001069c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Append limit (default 10) or limit greater than or equal to 1 and<br>less than or equal to 100 and printing error message if it exceeds:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231043972-f7baa0a8-a7b4-439b-98e0-135b4db2f3dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231044850-2eb3bc29-68c4-4939-9ac1-2b2772ac9b10.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231045310-8b1ef0fc-c253-485f-9fe9-37ae5f706741.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231045510-106f3483-629f-40ea-9d31-20f3cf68f2bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231046008-4608c6a3-a070-461c-88ce-7c7e95e53803.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing one asc filter applied (clearly label which column was chosen) - Name<br>column<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231046314-e83d4cce-0dbd-4b89-84bd-a4ecbcf2d7b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing one desc filter applied (clearly label which column was chosen)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231049179-d091dc5d-e1b6-4ef7-b2e0-19925cb16862.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Code should retrieve id (from request args) name, address, city, state, country,<br>zip, website from form. If id isn&#39;t present flash related error message and<br>redirect to company search and flash messages if they are missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231049370-0e722a3e-cf2c-4cc1-b509-8c9e35bd35ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing Update query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231049518-0aed9d12-693a-46d5-ab06-e593e500d419.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper SELECT query should be visible with the passed in data<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231049715-b7627d53-ee85-41e1-8526-83903ec5a156.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231050687-8361b7aa-8f93-473a-88ab-53c2d991fc33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231052067-a42fb23e-a2b9-41ef-a9d3-bf6c8bea7c3c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Caption: After edit - Name ( Lilly- Eli Lilly), address ( Bermuda drive<br>- mill rd),city (New jersey-edison)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231053844-c3b3b30b-4c8d-4743-8eb2-183ea7cf4a85.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before editing in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231053393-ddadb08a-0059-4ff5-91f8-f8fc33d56f33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After updating in database- Name (lilly- eli lilly, address (bermuda drive - mill<br>rd),city (brachburg - edison)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231056079-307435ae-8f12-4362-8882-dbb24be02f39.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete employee by id, if missing should flash the related message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231056189-9d5b2b0f-0de5-4c1a-93d5-870664b83543.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Redirect to employee search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231056366-cc93911b-5ff3-45ef-bf10-00843e0a8791.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All request args (minus id) are passed to the redirect route and success<br>flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231056557-61ca3365-a316-4104-b715-f6c04049e37a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting employees data in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231056760-378654f0-d07e-4763-b7a6-3914af960f7c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting employee data in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231056944-97630873-34e1-43d6-9c51-871ce5e8c24b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> After deleting record in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231057052-c5c584d2-0aab-4c50-ad7b-898ca00c0b7c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting record in database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231057303-4c3ba51f-817a-4511-9ef1-d572d63b7569.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete company by id, if missing should flash the related message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231057424-438f13c0-de55-4a87-87aa-5451aaa359a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Redirect to company search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231057524-fc3372a1-ea79-4e69-859b-3bf40aa9930c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> All request args (minus id) are passed to the redirect route and<br>success flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231057678-c7206d25-15e0-4330-b81a-05c4748bc664.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting company details in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231057787-364e9011-4284-4fc9-b410-add2bb448aaa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Caption: Before deleting company details in database - lilly<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231058013-932344e9-9c37-445a-ba36-1a4bf2827006.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> screenshot after deleting company details in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231058151-57029d64-3737-43c0-9aee-cd04e48b3877.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot after deleting the company from database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/231063315-d000fb91-4305-4c69-907b-38474d2c1e7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of test cases successfully passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>had some errors in some of the testcases and while deploying the yml<br>files to github but got them clarified by the professor and cleared with<br>his help on discord.<div>Got deep understanding on html and how the web pages<br>work.&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/vc435" target="_blank">Grading</a></td></tr></table>