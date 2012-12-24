$(document).ready(function () {
    $('input').live('focusout', function editTask() {
//        var isChecked = $("input:checkbox").is(":checked") ? 1 : 0;
//        alert(isChecked)
        var task_name = $(this).val();
        var task_id = $(this).attr('task_id')

//        $("input:checkbox").change(function() {
            if($("input:checkbox").is(":checked")) {
            }
        $.ajax({
            type: "POST",
            url: "/tasks_manager/" + task_id + "/edit_task/",
            data: {
                task_name : task_name
            }
        });
    });
    $('tr.main').live('click', function task_highlight() {
        $('.grid-row-selected').each(function () {
            $(this).toggleClass("grid-row-selected focused")
        })
        $(this).toggleClass("grid-row-selected focused")
    })
});
