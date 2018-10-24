var ProfilChangeHandler = {
    config: {
        field: "",
        elementId: "",
        inputType: "",
        inputClass: "form-control",
        inputId: "",
        inputValue: "",
        id: "",
        api: "",
    },
    createInput: function() {
        var element = document.getElementById(this.config.elementId);
        var inputField = document.createElement("input");
        inputField.setAttribute("type", this.config.inputType);
        inputField.setAttribute("class", this.config.inputClass);
        inputField.setAttribute("id", this.config.inputId);
        inputField.setAttribute("value", this.config.inputValue);
        element.classList.remove("cust-value");
        element.innerText = "";
        element.appendChild(inputField);
        document.getElementById(this.config.inputId).focus();
    },
    hideInput: function() {
        var element = document.getElementById(this.config.elementId);
        var textNode = document.getElementById(this.config.elementId).childNodes[0];
        var newValue =  textNode.value;
        element.classList.add("cust-value");
        element.removeChild(textNode);
        element.innerText = newValue;
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
            UserApi.saveData(JSON.stringify(obj), this.config.api);
        }
    },
    changeActionSelect: function() {
        val = document.getElementById(this.config.elementId).value;
        var obj = {}
        obj[this.config.field] = val;
        UserApi.saveData(JSON.stringify(obj), this.config.api);
    },
    configure: function(newConfig) {
        if (typeof newConfig === "object") {
          this.config = newConfig;
        }
    }
}