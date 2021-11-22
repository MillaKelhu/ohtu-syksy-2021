*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  kalle
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Set Username  maija
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Login After Successful Registration
    Go To Register From Login
    Registrate Successfully
    Log Out After Registration
    Set Username  jamesbond
    Set Password  skyfall007
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Go To Register From Login
    Registrate Unsuccessfully
    Return To Login From Register
    Set Username  heathcliff
    Set Password  cathy
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open

Go To Register From Login
    Click Link  Register
    Register Page Should Be Open

Return To Login From Register
    Click Link  Login

Try To Register
    Click Button  Register

Registrate Successfully
    Set Username  jamesbond
    Set Password  skyfall007
    Set Password Confirmation  skyfall007
    Try To Register

Log Out After Registration
    Click Link  Continue to main page
    Click Button  Logout
    Login Page Should Be Open

Registrate Unsuccessfully
    Set Username  heathcliff
    Set Password  cathy
    Set Password Confirmation  cathy
    Try To Register
