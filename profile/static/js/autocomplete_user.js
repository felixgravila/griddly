var users = new Array()
$(document).ready(function(){

    $('#del').live("click", function(){
        var recipient = $(this).next()
        users = jQuery.grep(users, function(value){
            return value != recipient.html()
        })
        $(this).remove()
        recipient.remove()
        //TODO: a place to make succes/fail
    })

    $('#new-recipient').keypress(function(event){
         if (event.keyCode == 13) {
            var new_user = $('#new-recipient').val()
            $.post('/user/check/', {'user': new_user}, function(data){
                if(data == 'exists'){
                     if (jQuery.inArray(new_user,users) == -1){
                        users.push(new_user)
                        $('#new-recipient').before('<span id="del">-</span><label id="recipient">'+$('#new-recipient').val()+'</label>')
                    }
                    $('#new-recipient').val('')
                }else{
                    $('#notifications_bar').html("User don't exists!").slideDown(200).delay(1000).slideUp(200);
                }
            });
            return false;
        }
    })
})
function put_users(users, div){
    $.each(users, function(index, value){
        div.before('<span id="del">-</span><label id="recipient">'+value+'</label>')
    })
}
