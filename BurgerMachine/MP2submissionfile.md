<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Burgers</td></tr>
<tr><td> <em>Student: </em> Vybhavi Chithapuram (vc435)</td></tr>
<tr><td> <em>Generated: </em> 3/22/2023 7:36:49 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/vc435" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb">https://gist.github.com/MattToegel/028db0e3fd2b20c1fb8e284b341292bb</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder BurgerMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226478408-4274ad9b-577d-4361-9ec5-f1ab14324e2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output showing costs that are defined in the data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/227060594-3aaa55e2-e9c8-4f86-beb7-1944cae4efdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code output displaying the value .<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>I used a for loop to go over each burger object in the<br>code above, and I used the sum() method to calculate the cost of<br>each burger object and return the overall cost.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226490660-734ec1a0-c594-418b-9955-842198e7ef5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for  OutOfStockException where proper user feedback and continued program<br>flow. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226491069-1397f21d-e0a3-4043-9654-07abe71d51bf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code for NeedsCleaningException is handled where it prompts the user to<br>type the word &#39;clean&#39; to clean the machine another words are ignored. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226491319-5f5546ba-fe51-4291-a6bf-2371833c1976.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code logic showing how InvalidChoiceExceptions are handled.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226491490-809045c8-3eff-49fd-a4a8-c55a22fbb184.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code logic showing how various ExceededRemainingChoicesExceptions are handled.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226491557-d4fad730-bf55-4d50-a65b-4a37413c0823.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of code logic showing how the InvalidPaymentException is handled.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div>OutofStockException:&nbsp;</div><div>When a user wishes to add a choice from the options but there<br>isn't a quantity available they can utilize this exception.</div><div><br></div><div>NeedsCleaningException:</div><div>This exception implies that the<br>machine needs to be cleaned in so it can operate properly.Till the user<br>provides the proper input to clean the machine, the while loop will remain.The<br>program will continue and the loop will be broken if it reads the<br>input correctly.</div><div><br></div><div>InvalidChoiceException:</div><div>When the user selects an item from the options to add to<br>the list but there aren't enough quantities availability to go around,the OutOfStockException is<br>raised.</div><div><br></div><div>ExceededRemainingChoicesException:</div><div>It is used if the user's selection for the patties and toppings exceeds<br>"3" options.</div><div><br></div><div>InvalidPaymentException:</div><div>If the user enters a different amount than what is displayed, the<br>InvalidPaymentException is raised,and the user is prompted to try again with the correct<br>amount.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226495412-9cc7eddc-526a-4e28-9f3a-b4952999ea41.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of test case checking if the bun is in the first selection<br>stage.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226495451-a421c8d7-2ef9-4fba-b461-5d9a5c481e5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case check if patties can be added only if they<br>are in stock.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226495953-947d042f-e26a-4bf0-a534-cc831eec53df.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case to  check if toppings can be added only<br>if they are in stock. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226496036-2e1ffcfa-407b-4270-a289-5c73171c0352.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case to check if max patties added in any combination<br>is three.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226496083-90bfd8c2-9e7f-4c86-97b4-28f7452fe141.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case to check if max toppings added in any combination<br>is three.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226496141-018fac4c-6d9d-4fff-82d5-e46d8b9a65bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case to check the total cost  of the purchase<br>properly based on the choices.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226496213-97c6e42e-540b-4824-9b7d-9578fbc886c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of test case calculating  Total Sales .<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226496275-81a091e0-f764-4b28-8929-cf5b3f5d174f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of test case calculating Total burgers being incremented for each purchase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/226509469-15492514-2fc0-46b4-bae9-bd8f98b97f8e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing  tests cases 1-8 passing <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>Test_first_selection:</div><div>This test determines whether or not the bun is the first selection stage.</div><div><br></div><div>Test_patties_in_stock:</div><div>In<br>order to determine whether the patties can be added again or not, the<br>burger machine item quantity is changed to 1,and if the item is added,<br>an OutOfStock Exception will be raised.</div><div><br></div><div>Test_toppings_in_stock:</div><div>By setting the amount of the first topping's<br>machine to 1,this test initially shows that there is only one unit of<br>that topping in stock and shows that there is only one in the<br>quantity of that topping,if the same topping is chosen twice, it raises an<br>OutOfStock Exception.</div><div><br></div><div>Test_max_patties:</div><div>This exception is used as a topping for a loop. The max<br>toppings is used three times,if more than three patties are added, ExceededRemainingChoices will<br>be raised.</div><div><br></div><div>Test_total_cost:</div><div>When added a bun, a few options of patties from the list<br>and toppings,all these ingredients are added together. The sum is calculated from the<br>inputs aredeclared that the sum is equal to the cost that is determined<br>.</div><div><br></div><div>Test_total_sales:</div><div>A bun, few of the list's options for patties, and toppings are added.Three<br>separate burgers were included with a variety of options, and&nbsp; payments are made<br>for all three of them The total sales were equivalent to the cost<br>of the three burgers.</div><div><br></div><div>Test_total_burgers:</div><div>added 3 separate burgers, accepted acceptable payments for 3 of<br>them,and stated that the total number of burgers was 3.Used the pytest fixture<br>second order wchich is equated to 0 and total burgers to 3.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vybhavi1212/IS601-006/pull/12">https://github.com/vybhavi1212/IS601-006/pull/12</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>I faced issue while activating the venv&nbsp; as the<span style="color: rgb(34, 34, 34);<br>font-family: Arial, Helvetica, sans-serif; font-size: small;">&nbsp;folder didn&#39;t get to github, I had to<br>remove the file.</span>&nbsp;I have again created a global venv folder and&nbsp; by using<br>different set of commands I was able to activate.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123990668/227053775-c3e2b16c-4f4f-4a5d-946b-57a9284d27bb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of  execution of program when 3 different combinations of burgers are<br>selected.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-006-S23/is601-mini-project-2-burgers/grade/vc435" target="_blank">Grading</a></td></tr></table>