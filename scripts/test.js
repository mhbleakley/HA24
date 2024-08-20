$(document).ready(function(){

$("button").click(function(){
    $.get("test.txt", function(data, status){
    alert("Data: " + data + "\nStatus: " + status);
    });
});

});