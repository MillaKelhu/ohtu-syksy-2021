*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  rose  itsbeen80years
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  khalleesi8
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  v  november5
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  elsa  2cool4u
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  harry  hogwarts
    Output Should Contain  Password must contain at least one number or special character

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command