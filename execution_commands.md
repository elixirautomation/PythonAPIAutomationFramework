##### Test execution based on 'marks/suites' (smoke, regression)
```sh
py.cleanup -p && py.test -m smoke --alluredir ExecutionReports/
py.cleanup -p && py.test -m regression --alluredir ExecutionReports/
```

##### Report Portal Commands
```sh
py.cleanup -p && py.test --reportportal
py.cleanup -p && py.test -m regression --reportportal
py.cleanup -p && py.test -m smoke --alluredir ExecutionReports/ --reportportal
```

##### Trigger Allure Reports
```sh
allure serve ExecutionReports
```
