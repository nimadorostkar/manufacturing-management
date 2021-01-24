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
        { id: 3, pid: 2, name: "مونتاژ نیرو خانگی", title: "نیرو خانگی", img: "img/asembeling.png", tags: ["نیرو خانگی"] },
        { id: 4, pid: 3, name: "مغزی سوکت هالوژن", title: "نیمه آماده", img: "img/maghzi.png" },
        { id: 5, pid: 3, name: "سیم ترمینال خورده", title: "نیمه آماده", img: "img/wireter.png" },
        { id: 6, pid: 3, name: "کش بسته بندی", title: "قطعه خریداری شده", content:"gggg", img: "img/kesh.jpg", tags: ["قطعه خریداری شده"] },
        { id: 7, pid: 5, name: "برش سیم و پرچ", title: "صائمیان", img: "img/wirecut.png" },
        { id: 8, pid: 4, name: "بسته بندی پلاتین زنی", title: "خیرآباد", img: "img/packing.png" },
        { id: 9, pid: 7, name: "ترمینال MR16", title: "قطعه خریداری شده", img: "img/mr16.jpg", tags: ["قطعه خریداری شده"] },
        { id: 10, pid: 7, name: "کلاف ۵۰۰ متری", title: "قطعه خریداری شده", img: "img/wire.jpg", tags: ["قطعه خریداری شده"] },
        { id: 11, pid: 8, name: "تزریق مغزی خیرآباد", title: "تزریق خیرآباد", img: "img/wire.jpg" },
        { id: 12, pid: 8, name: "نایلون", title: "قطعه خریداری شده", img: "img/naylon.jpg", tags: ["قطعه خریداری شده"] },
        { id: 13, pid: 8, name: "منگنه", title: "قطعه خریداری شده", img: "img/mangane.jpg", tags: ["قطعه خریداری شده"] },
        { id: 14, pid: 11, name: "مواد PC", title: "قطعه خریداری شده", img: "img/pc.jpg", tags: ["قطعه خریداری شده"] },
        { id: 15, pid: 11, name: "کیسه", title: "قطعه خریداری شده", img: "img/kise.jpg", tags: ["قطعه خریداری شده"] },
        { id: 18, pid: 11, name: "نخ", title: "قطعه خریداری شده", content:"تست تست تست ۳۳۳ تست", img: "img/nakh.jpg", tags: ["قطعه خریداری شده"] },
      ]);


};
