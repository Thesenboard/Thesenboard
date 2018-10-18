var ProfilChangeHandler = {
    config: {
        field: "",
        elementId: "",
        inputType: "",
        inputClass: "form-control",
        inputId: "",
        inputValue: "",
        id: ""
    },
    createInput: function() {
        var inputField = document.createElement("input");
        inputField.setAttribute("type", this.config.inputType);
        inputField.setAttribute("class", this.config.inputClass);
        inputField.setAttribute("id", this.config.inputId);
        inputField.setAttribute("value", this.config.inputValue);
        document.getElementById(this.config.elementId).innerText = "";
        document.getElementById(this.config.elementId).appendChild(inputField);
        document.getElementById(this.config.inputId).focus();
    },
    hideInput: function() {
        var textNode = document.getElementById(this.config.elementId).childNodes[0];
        var newValue =  textNode.value;
        document.getElementById(this.config.elementId).removeChild(textNode);
        document.getElementById(this.config.elementId).innerText = newValue;
        return newValue;
    },
    changeAction: function () {
        if(document.getElementById(this.config.id).innerText === "Bearbeiten") {
            document.getElementById(this.config.id).innerText = "Ändern";
            this.createInput();
        } else {
            document.getElementById(this.config.id).innerText = "Bearbeiten"
            var newValue = this.hideInput(this.config.elementId, this.config.id);
            var obj = {}
            obj[this.config.field] = newValue;
            UserApi.saveData(JSON.stringify(obj));
        }
    },
    configure: function(newConfig) {
        if (typeof newConfig === "object") {
          this.config = newConfig;
        }
    }
}