$(document).ready(function () {
    $('#project_name').live('focusout', function editProject() {
        var project_name = $("#project_name").val();
        var project_id = $(this).attr('project_id')
        $.ajax({
            type: "POST",
            url: "/tasks_manager/" + project_id + "/edit_project/",
            data: {
                project_name : project_name
            },
            success: function (message) {
                $("#projects").html(message);
            }
        });
    });
});