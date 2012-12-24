$(document).ready(function() {
    $("#add_project_button").on("click", function createProject() {
        $.ajax({
            type: "POST",
            url: "/tasks_manager/create_project",
            success: function (message) {
                $("#projects").html(message);
            }
        });
    });
});