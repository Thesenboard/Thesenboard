$(document).ready(function () {
    'use strict';
    try{
        document.getElementById("benutzer").addEventListener("click", function() {
            var inputValue;
            var elementId = "user";
            inputValue = document.getElementById(elementId).innerText;
            if (inputValue === undefined) {
                var val = document.getElementById(elementId).childNodes[0];
                inputValue = val.value;
            }
            ProfilChangeHandler.configure({
                field: "username",
                elementId: elementId,
                inputType: "text",
                inputClass: "form-control",
                inputId: HelperFunctions.createId(),
                inputValue: inputValue,
                id: $(this)[0].id,
                api: 'user'
            });
            ProfilChangeHandler.changeAction();
        });
        document.getElementById("email").addEventListener("click", function() {
            var inputValue;
            var elementId = "mail";
            inputValue = document.getElementById(elementId).innerText;
            if (inputValue === undefined) {
                var val = document.getElementById(elementId).childNodes[0];
                inputValue = val.value;
            }
            ProfilChangeHandler.configure({
                field: "email",
                elementId: elementId,
                inputType: "email",
                inputClass: "form-control",
                inputId: HelperFunctions.createId(),
                inputValue: inputValue,
                id: $(this)[0].id,
                api: 'user'
            });
            ProfilChangeHandler.changeAction();
        });
        document.getElementById("vorname").addEventListener("click", function() {
            var inputValue;
            var elementId = "vname";
            inputValue = document.getElementById(elementId).innerText;
            if (inputValue === undefined) {
                var val = document.getElementById(elementId).childNodes[0];
                inputValue = val.value;
            }
            ProfilChangeHandler.configure({
                field: "first_name",
                elementId: elementId,
                inputType: "text",
                inputClass: "form-control",
                inputId: HelperFunctions.createId(),
                inputValue: inputValue,
                id: $(this)[0].id,
                api: 'user'
            });
            ProfilChangeHandler.changeAction();
        });
        document.getElementById("nachname").addEventListener("click", function() {
            var inputValue;
            var elementId = "nname";
            inputValue = document.getElementById(elementId).innerText;
            if (inputValue === undefined) {
                var val = document.getElementById(elementId).childNodes[0];
                inputValue = val.value;
            }
            ProfilChangeHandler.configure({
                field: "last_name",
                elementId: elementId,
                inputType: "text",
                inputClass: "form-control",
                inputId: HelperFunctions.createId(),
                inputValue: inputValue,
                id: $(this)[0].id,
                api: 'user'
            });
            ProfilChangeHandler.changeAction();
        });
        document.getElementById("anzeigeart").addEventListener("click", function() {
            var elementId = "aart";
            ProfilChangeHandler.configure({
                field: "user_visibility",
                elementId: elementId,
                api: 'user'
            });
            ProfilChangeHandler.changeActionSelect();
        });
        document.getElementById("tags").addEventListener("click", function() {
            var inputValue;
            var elementId = "utags";
            inputValue = document.getElementById(elementId).innerText;
            if (inputValue === undefined) {
                var val = document.getElementById(elementId).childNodes[0];
                inputValue = val.value;
            }
            ProfilChangeHandler.configure({
                field: "user_tags",
                elementId: elementId,
                inputType: "text",
                inputClass: "form-control",
                inputId: HelperFunctions.createId(),
                inputValue: inputValue,
                id: $(this)[0].id,
                api: 'user'
            });
            ProfilChangeHandler.changeAction();
        });
    } catch(e) {
        // do nothing...
    }

});