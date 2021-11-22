*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  mina
    Set Password  murray1897
    Set Password Confirmation  murray1897
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  v
    Set Password  5november
    Set Password Confirmation  5november
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  elsa
    Set Password  2cool4u
    Set Password Confirmation  2cool4u
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Nonmatching Password And Password Confirmation
    Set Username  tolkien
    Set Password  hobbit1937
    Set Password Confirmation  lordoftherings1954
    Submit Credentials
    Register Should Fail With Message  Password and confirmation don't match

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open
