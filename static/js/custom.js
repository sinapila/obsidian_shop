function sendComment(articleid) {
    // console.log('hi')
    var comment = $("#CommentText").val();
    var parentid = $("#parent_id").val();


    $.get('/articles/add-article-comment', {
        comment,
        articleid,
        parentid: parentid

    }).then(res => {
        console.log(res)
        $("#comments_area").html(res)
        $("#CommentText").val("");
        $("#parent_id").val('');
        document.getElementById('command_' + comment.id).scrollIntoView({behavior: "smooth"})

    })
}

function FillParentId(parentid) {
    $("#parent_id").val(parentid)
    document.getElementById('command_form').scrollIntoView({behavior: "smooth"})
}

function add_product_to_order(productId) {
    const productCount = $('#product-count').val();
    $.get('/order/add-to-order?product_id=' + productId + '&count=' + productCount).then(res => {
        Swal.fire({
            title: 'اعلان',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/account/login';
            }
        })


        /*if (res.status === 'success') {
            Swal.fire({
                title: 'اعلان',
                text: "محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد",
                icon: 'success',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'باشه ممنون'
            });
        } else if (res.status === 'not_found') {
            Swal.fire({
                title: 'اعلان',
                text: "محصول مورد نظر یافت نشد",
                icon: 'error',
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: 'باشه ممنون'
            });
        }*/
    });
}

