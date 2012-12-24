$(document).ready(function() {
    $('input.task-row-text-input').live('keyup', function createTask(e){
        if(e.keyCode == 13){
            var project_id = $('a.list-item.selected').attr('project_id')
            $.ajax({
                type: "POST",
                url: "/tasks_manager/" + project_id + "/create_task",
                success: function (message) {
                    $("#tasks_table").html(message);
                }
            });
        }
    });
});
