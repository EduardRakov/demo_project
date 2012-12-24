$(document).ready(function () {
    $('a.list-item').live('click', function () {
        var project_id = $(this).attr('project_id')
        $.ajax({
            type: "POST",
            url: "/tasks_manager/current_project/",
            data: {
                project_id : project_id
            },
            success: function (message) {
                $("#center_pane_container").html(message);
            }
        });
        $("a.list-item.selected").each(function () {
            $(this).toggleClass("selected")
        });
        $(this).toggleClass("selected")
    });
});
//});
//var elm = $("#projects");
//$('#projects').on('click', 'a' function () {
//});
//    $('#projects').load($(this).attr('href'));
//    this.className = "list-item selected";
//    event.preventDefault();

//        $("a.list-item.selected").each(function(){
//            $(this).toggleClass("selected")
//        });