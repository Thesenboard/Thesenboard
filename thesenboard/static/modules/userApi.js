var UserApi = {
    saveData: function(jsonData, api) {
        var csrftoken = UserApi.getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!UserApi.csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            contentType : 'application/json',
            processData : false
        });
        $.ajax({
           url: '/'+api+'/',
           type: 'PUT',
           data: jsonData,
           success: function(response) {
             // does nothing yet...
           }
        });
    },
    getCookie: function(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    },
    csrfSafeMethod: function(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
}

