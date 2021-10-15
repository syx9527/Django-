var username = $("#user_name").text();

// 获取文章列表
$(document).ready(function () {

    $.ajax({
        url: "/query_article_list/",
        type: "post",

        username: "{{ user.username }}",
        data: {
            name: 'all',
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            username: username,
        },

        success: function (data) {

            $('#article_list').html(data.content_html);

        }
    });

    $.ajax({
        url: "/query_tag_list/",
        type: "post",

        username: "{{ user.username }}",
        data: {
            name: 'all',
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            username: username,
        },

        success: function (data) {

            $('#tag_list').html(data.content_html);

        }
    });

    $.ajax({
        url: "/query_cate_list/",
        type: "post",

        username: "{{ user.username }}",
        data: {
            name: 'all',
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            username: username,
        },

        success: function (data) {

            $('#cate_list').html(data.content_html);

        }
    });

    // 获取归档列表
    $.ajax({
        url: "/query_month_list/",
        type: "post",

        username: "{{ user.username }}",
        data: {
            name: 'all',
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            username: username,
        },

        success: function (data) {

            $('#year_month').html(data.content_html);

        }
    });

});


// 触发点击事件，js渲染后点击失效，已经解决
$(document).on("click", ".author_btn", function () {
    var id = this.id;
    var name = this.getAttribute("name");
    console.log(id, name)
    $.ajax({
        url: "/query_article_list/",
        type: "post",

        username: "{{ user.username }}",
        data: {
            id: id,
            name: name,
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
            username: username,
        },

        success: function (data) {

            $('#article_list').html(data.content_html);

        }
    })
});


