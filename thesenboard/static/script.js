$(function() {
    'use strict';

    var elementId;
    var inputType;
    var inputClass = "form-control";
    var inputId;
    var inputValue;

    try{

        document.getElementById("benutzer").addEventListener("click", function() {
            elementId = "user";
            inputType = "text";
            inputValue = document.getElementById("user").innerText;
            inputId = inputValue.replace(" ", "_");
            changeAction($(this)[0].id);
        });
        document.getElementById("email").addEventListener("click", function() {
            elementId = "mail";
            inputType = "email";
            inputValue = document.getElementById("mail").innerText;
            inputId = inputValue.replace(" ", "_");
            changeAction($(this)[0].id);
        });
        document.getElementById("vorname").addEventListener("click", function() {
            elementId = "vname";
            inputType = "vorname";
            inputValue = document.getElementById("vname").innerText;
            inputId = inputValue.replace(" ", "_");
            changeAction($(this)[0].id);
        });
        document.getElementById("nachname").addEventListener("click", function() {
            elementId = "nname";
            inputType = "nachname";
            inputValue = document.getElementById("nname").innerText;
            inputId = inputValue.replace(" ", "_");
            changeAction($(this)[0].id);
        });
    } catch(e) {

    }


    function createInput(elementId, inputType, inputClass, inputId, inputValue) {
        var inputField = document.createElement("input");
        inputField.setAttribute("type", inputType);
        inputField.setAttribute("class", inputClass);
        inputField.setAttribute("id", inputId);
        inputField.setAttribute("value", inputValue);
        document.getElementById(elementId).innerText = "";
        document.getElementById(elementId).appendChild(inputField);
        document.getElementById(inputId).focus();
    }

    function hideInput(elementId, inputId) {
        document.getElementById(inputId).innerText = "Bearbeiten";
        var textNode = document.getElementById(elementId).childNodes[0];
        var neuerName =  textNode.value;
        document.getElementById(elementId).removeChild(textNode);
        document.getElementById(elementId).innerText = neuerName;
    }

    function changeAction(id) {
        if(document.getElementById(id).innerText === "Bearbeiten") {
            document.getElementById(id).innerText = "Ändern";
            createInput(elementId, inputType, inputClass, inputId, inputValue);
        } else {
            hideInput(elementId, id);
        }
    }

});