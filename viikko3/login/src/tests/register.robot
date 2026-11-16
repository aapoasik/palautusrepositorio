*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Reset Application And Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Reset Application And Go To Register Page
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Registration Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Reset Application And Go To Register Page
    Set Username  kalle123
    Set Password  k
    Set Password Confirmation  k
    Click  button >> text=Register
    Registration Should Fail With Message  Password is too short

Register With Username That Is Already In Use
    Reset Application And Go To Register Page
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Registration Should Succeed
    Go To Register Page
    Register Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Registration Should Fail With Message  User with username kalle already exists

*** Keywords ***


Registration Should Succeed
    Welcome Page Should Be Open

Welcome Page Should Be Open
    Get Title  ==  Welcome to Ohtu Application!

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}
