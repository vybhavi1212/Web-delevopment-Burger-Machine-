<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Venkata Sai Pragna Garisa (vg473)</td></tr>
<tr><td> <em>Generated: </em> 4/9/2023 12:45:56 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/vg473" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230746829-230c941e-e726-49a9-b3dd-0718921c9441.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230746964-8ea8ecb0-4528-42a3-b27c-d9462501296d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB Tables from VS code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230747092-38e0350e-8852-4811-9bfe-ce62062d442f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code checking whether the file is .csv or not:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230747154-eb554c75-7f39-48b6-b367-a72c163daf66.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code reading file and appending into dictonary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230747257-9b89ca6f-52d4-44ab-b516-458241129dc2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code of processed records showing in flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230747358-ab2f7131-f51e-472e-9352-5e5e35ed87cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code if nothing was loaded<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230747593-3d25b5dc-a85d-435a-b3f8-0d9160a8b27e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Import successful and Count of records<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230747846-d4a59c61-aea9-4791-8b6e-3be217aab352.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid file message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230747881-c22b6f48-e4e7-4b9c-b5a5-1fa5988f3713.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message if submitted without attachment<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230747962-3ea71610-1bdd-4a2d-8ffb-809cadb249d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employees data in table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230747935-8f7b685a-3895-4dfc-af19-32c919ab603f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Companies data in table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230748080-c8e762b9-d64c-4acb-94f0-b90e31fac22d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Retrieving first_name, last_name, company (id), email with flash messages if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230748129-a92ce008-8d35-4a24-83b6-1e676d5d0533.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Insert query and flash message to print exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230748212-56f2e6fa-5eb5-4401-abef-8b27386bc1ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message if submitted without filling <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230748294-9b0775e7-3972-450f-abdd-a15c2fca9ef6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230748325-7762d4fa-5dce-4e12-bc07-8858b9b69c0f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230748404-4e3a8f02-84f7-40d6-924c-f7bf1f2cf35a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Last_name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230748461-320e1fcc-92d3-47da-8587-036a155661c3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230748540-ecb0bec8-361f-4710-9e6a-cadb3b3715ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New Employee record data - Venkata sai pragna<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749076-5796fba9-4906-4464-beb2-cdebc2eef985.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Select query to retrive data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749148-0a02cc53-df15-4244-9ca7-72b86e282bea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Checking requested args<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749198-e309a4b5-dbc4-4652-a4f2-27209e29fe3d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Appending like filter for First_name,last_name,email,company_id<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749285-1c61c794-81ce-4a86-a4c6-5db4e512d26d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Append sorting allowed columns<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749417-07570f63-ec21-444a-a443-ac4b453aedbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message if limit is out of bond<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749542-8c8f47f7-7079-46b8-a11e-abb3186a9afc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Exception handling message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749574-74969ae1-c609-4272-a24b-e04cf7a3ffbf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749606-d62d2892-d6de-4a74-aacc-2b0e7bf3e40a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749652-54b88bf3-9399-4e60-82fd-031e30538943.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749714-4d56fed7-9fe4-47bd-b140-3d82ec604346.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Results with company filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749770-398d7838-07a3-4937-be76-6152e831f0bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Results with asc order filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749804-ed25207c-e84d-4fb2-a7d7-f7a223e09d9b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Results with desc order filter applied<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749933-85e1c805-de40-4538-a837-bfc4a6ee5537.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) first_name, last_name, company (id), email from<br>form. Missing id should be handled with a flash message and redirected back<br>to employee search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230749976-bdf848cf-6f04-4671-bf04-18eb4ae54cc1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Flash message first_name, last_name, email, company(not required)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750019-1b10f69e-d03c-46a9-8ea3-1a21bbd7faee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>update query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750058-683956b1-f3e8-4b10-9d06-1a9b7416e950.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except blocks (two) should have a user friendly message flashed and a print()<br>of the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750084-9e2bc884-19fb-40da-9a8f-55a008a27c15.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper SELECT query should be visible<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750132-fc8c0a53-31fe-4848-9079-3db1f1ca39cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee data should be passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750187-c2cdc6e8-c39e-4e10-9839-67b9f6c8a17d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before editing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750511-e8dd3858-35a1-45ab-8c24-3b5920717500.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After editing data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750237-c33b091e-cc99-4509-86ed-cf26c8178986.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before editing in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750466-81465cb0-6879-4550-ac2e-817fdc9fc91c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>editing last name (garisa-Nagisetty) , Company (no company-c4 network inc)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750569-774ab985-0542-4c16-a3b4-8fa0462b96a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieve form data for name, address, city, state, country, zip, website and<br>flash messages if missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750610-8a0e5343-9d32-4310-ad95-440175b799ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Insert Query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750638-39f72aa0-9b38-44c2-874c-f831716c4bf4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user-friendly message flashed and a print() of the<br>exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750720-6a70c9ce-f1dd-440e-8c53-03748aa1ae0a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show filled in valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750751-ddf40c91-807f-41d3-b847-cd09bbb76b7b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750830-1eb7dec3-a448-477f-8607-578f650ff7f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message for company name, address, city, zip code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750889-5d4119e1-f076-46cc-9e90-800d78b072e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message, if country is missing<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750910-408d0912-1d4d-493f-8f14-9a70a68bc7cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message if state is missing<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230750955-2f5931ff-36ad-4eb5-b1cd-fa039160447c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should include the valid company data shown previously (NJIT- last one id=45)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751074-196215e4-4b8c-4c2c-9447-17c636d5047a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query should fetch id, name, address, city, country, state, zip, website, employee<br>count (as employee) for the company (likely a sub-query is needed)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751110-f2024e23-11bc-4464-8a8f-f5ea24204db6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Check request args for name, country, state, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751156-766857b7-e042-4a55-8f4d-751fd329a839.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append an equality filter for state if provided,if country provided and name:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751239-2d7a9744-03d9-479c-a51b-346f553f4f63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append sorting if column and order are provided and within the allows columsn<br>and allowed order asc,desc allowed_columns = [&quot;name&quot;, &quot;city&quot;, &quot;country&quot;, &quot;state&quot;]<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751284-0fe73c34-0fdc-4b7c-a5a9-bcf334c098af.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>append limit (default 10) or limit greater than or equal to 1 and<br>less than or equal to 100 and printing error message if it exceeds:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751338-79a30054-b260-4b7e-a333-2447ea44217e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Except block should have a user friendly message flashed and a print() of<br>the exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751427-b9508fc6-7890-4d18-9993-d3511958fb34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751459-69897da6-f86d-486b-b0f1-8648660b6328.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751505-b7cc167d-e6eb-4238-a185-2f4552da79ae.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751542-d53f7432-c69c-4f0d-a0cf-e5fd36802ee6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show one asc filter applied (clearly label which column was chosen) - Name<br>column:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751579-929d2c65-92c2-4d2f-b2ca-3b99919448cb.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Show one desc filter applied (clearly label which column was chosen) - Name&lt;br&gt;column&lt;br&gt;
</code></pre>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751707-a8932240-4202-49f3-a42a-9a582ac8cb63.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) name, address, city, state, country, zip,<br>website from form. If id isn&#39;t present flash related error message and redirect<br>to company search and flash messages if they are missing:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751757-0af15579-7fde-4888-81fe-05f7dad73dff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751835-4e832d15-da54-4deb-aaa8-45bedf237854.png"/></td></tr>
<tr><td> <em>Caption:</em> <pre><code>Proper SELECT query should be visible with the passed in data&lt;br&gt;
</code></pre>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230751880-63944e33-58ef-4160-bca6-394d3d20f53a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company data should be passed to the render_template()  <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230752063-ea7018ca-9794-47d1-9b26-0a4b740bd529.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Show data before an edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230752239-6d4e324f-66e2-4ccc-b0e2-f696222c607f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After edit - Name (NJIT- NJIT education), address (passaic ave- passaic ave 1),city<br>(Newark-New jersey)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230752190-53db5922-7a6c-4639-9c12-fb3836925a93.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before edit in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230752337-ad12d6ab-fb35-447d-a1d9-0bd5b2be8ba9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After edit in database- Name (NJIT- NJIT education), address (passaic ave- passaic ave<br>1),city (Newark-New jersey):<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230752694-6ddcf2db-0622-4c24-8a7b-1659043d9882.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete employee by id, if missing should flash the related message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753104-1dba93ae-ecac-4907-bbd0-1637b5629674.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Redirect to employee search<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753162-aea9e80c-d073-47fb-ba5f-9cd8cc8a4665.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All request args (minus id) are passed to the redirect route and success<br>flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753365-b89d1c61-5059-4b98-a6f7-c5d1d9771258.png"/></td></tr>
<tr><td> <em>Caption:</em> <p> Before deleting employee data in database:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753464-3c7163f2-bb0e-45d2-bdc5-815cad589efa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting employee data in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753520-e38c57c4-8e18-40b4-a456-50c931efeb03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting record in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753573-ffd495a8-8b58-464a-8452-c6f822f4d868.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting record in database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230752694-6ddcf2db-0622-4c24-8a7b-1659043d9882.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete company by id, if missing should flash the related message:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753287-c3ef5bc8-fc9f-48de-a4b2-afdb9b1d857e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Redirect to company search:<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753325-050319a0-f21e-415c-b5e0-c49ca94230d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All request args (minus id) are passed to the redirect route and success<br>flash message:<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753752-1c8ccd3a-ab7b-424d-87c3-57ef041a88a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting company details in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753808-a4e8d6ac-9b57-420f-86a8-d64ab983bb4f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting company details in database - NJIT EDUCATION(last)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753852-2ffca9cf-f898-4669-9811-0b2142ec0e44.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting company details in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230753891-f2018f84-41b3-4b42-bdfe-a173e364ff25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting company details in website<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230754097-77e3fa4c-1607-4300-bfc2-d08ee5fba5cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_upload_csv.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230754146-0a119cf0-455a-41fc-b58e-055475bcfb40.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_add_company.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230754199-6b08d571-5105-4fc1-aadc-638b0905deaa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_add_employee.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230754239-9f6fd9aa-17f9-4fe2-9380-152a00400c34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_edit_employee.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230754271-2c807a4a-d426-4d2f-b41a-9d5557177905.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_edit_company.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230754316-72d5e266-8781-4dce-95d6-2844a8318fe0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_search_company.py<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123420485/230754627-5272f553-2020-4c27-afe3-06046b650246.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_search_employee.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <hr>1. Clear understing of HTML<div>2. Faced issue while connecting to database with python</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-3-business-management/grade/vg473" target="_blank">Grading</a></td></tr></table>