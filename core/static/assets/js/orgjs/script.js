window.onload = function () {
    OrgChart.templates.ana.plus = '<circle cx="15" cy="15" r="15" fill="#ffffff" stroke="#aeaeae" stroke-width="1"></circle>'
        + '<text text-anchor="middle" style="font-size: 18px;cursor:pointer;" fill="#757575" x="15" y="22">{collapsed-children-count}</text>';

    var chart = new OrgChart(document.getElementById("tree"), {
        template: "ana",
        enableDragDrop: true,
        assistantSeparation: 170,
        align: OrgChart.ORIENTATION,
        toolbar: {
            fullScreen: true,
            zoom: true,
            fit: true,
            expandAll: true
        },
        tags: {
                "محصول نهایی": {
                    template: "rony"
                },
                "----": {
                    template: "polina"
                },
                "قطعه خریداری شده": {
                    template: "ula"
                },
                "---": {
                    template: "ana"
                },
                "نیرو خانگی": {
                    template: "belinda"
                }
            },
        nodeBinding: {
            field_0: "name",
            field_1: "title",
            field_2: "content",
            img_0: "img"
        },
    });

    chart.load([
        { id: 1, pid: 0, name: "سوکت هالوژن", title: "محصول نهایی", content:"تست تست تست ۳۳۳ تست", img: "img/sooket_halooj.jpg", tags: ["محصول نهایی"] },
        { id: 2, pid: 1, name: "بسته بندی نیرو خانگی", title: "نیرو خانگی", img: "img/packing.png", tags: ["نیرو خانگی"] },
        { id: 3, pid: 1, name: "مونتاژ نیرو خانگی", title: "نیرو خانگی", img: "img/asembeling.png", tags: ["نیرو خانگی"] },
        { id: 4, pid: 2, name: "کیسه", title: "قطعه خریداری شده", img: "img/kise.jpg", tags: ["قطعه خریداری شده"] }

      ]);


};