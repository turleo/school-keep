(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-0e81f762"],{"1f05":function(t,n,e){"use strict";e.r(n);var o=function(){var t=this,n=t.$createElement,e=t._self._c||n;return e("md-steppers",{attrs:{"md-active-step":t.active,"md-linear":""},on:{"update:mdActiveStep":function(n){t.active=n},"update:md-active-step":function(n){t.active=n}}},[e("md-step",{attrs:{id:"first","md-label":t.$t("onboarding.title"),"md-done":t.welcome_now},on:{"update:mdDone":function(n){t.welcome_now=n},"update:md-done":function(n){t.welcome_now=n}}},[e("h1",[t._v(t._s(t.$t("onboarding.welcome")))]),e("h2",[t._v(t._s(t.$t("onboarding.welcome_subtitle")))]),e("md-button",{staticClass:"md-raised md-primary",on:{click:function(n){return t.setDone("first","subjects_now")}}},[t._v(t._s(t.$t("onboarding.start")))]),e("br"),e("router-link",{attrs:{to:"settings"}},[e("md-button",{staticClass:"md-primary"},[t._v(t._s(t.$t("onboarding.skip")))])],1)],1),e("md-step",{attrs:{id:"subjects_now","md-label":t.$t("onboarding.step2"),"md-done":t.subjects_now},on:{"update:mdDone":function(n){t.subjects_now=n},"update:md-done":function(n){t.subjects_now=n}}},[e("h1",[t._v(t._s(t.$t("onboarding.subjects_title")))]),e("Subjects"),e("md-button",{staticClass:"md-raised md-primary",on:{click:function(n){return t.setDone("subjects_now","bells_now")}}},[t._v(t._s(t.$t("onboarding.next")))])],1),e("md-step",{attrs:{id:"bells_now","md-label":t.$t("onboarding.step3"),"md-done":t.bells_now},on:{"update:mdDone":function(n){t.bells_now=n},"update:md-done":function(n){t.bells_now=n}}},[e("h1",[t._v(t._s(t.$t("onboarding.bells_title")))]),e("Bells"),e("md-button",{staticClass:"md-raised md-primary",on:{click:function(n){return t.setDone("bells_now","timetable_now")}}},[t._v(t._s(t.$t("onboarding.next")))])],1),e("md-step",{attrs:{id:"timetable_now","md-label":t.$t("onboarding.step4"),"md-done":t.timetable_now},on:{"update:mdDone":function(n){t.timetable_now=n},"update:md-done":function(n){t.timetable_now=n}}},[e("h1",[t._v(t._s(t.$t("onboarding.timetable_title")))]),e("p",[t._v(t._s(t.$t("onboarding.timetable_subtitle")))]),e("Timetable"),e("md-button",{staticClass:"md-raised md-primary",on:{click:function(n){return t.setDone("timetable_now","congratulations")}}},[t._v(t._s(t.$t("onboarding.next")))])],1),e("md-step",{attrs:{id:"congratulations","md-label":t.$t("onboarding.step5"),"md-done":t.welcome_now},on:{"update:mdDone":function(n){t.welcome_now=n},"update:md-done":function(n){t.welcome_now=n}}},[e("p",{staticStyle:{"font-size":"250px","margin-bottom":"150px","margin-top":"150px"}},[t._v("🥳")]),e("h1",[t._v(t._s(t.$t("onboarding.congratulations.title")))]),e("a",{on:{click:function(n){t.$router.push("/").then((function(){t.$router.go()}))}}},[t._v(t._s(t.$t("onboarding.congratulations.link")))])])],1)},i=[],s=e("179e"),a=e("536a"),d=e("df23"),c={name:"OnBoarding",components:{Timetable:d["a"],Bells:a["a"],Subjects:s["a"]},data:function(){return{active:"first",welcome_now:!1,subjects_now:!1,bells_now:!1,timetable_now:!1,congratulations:!1}},methods:{setDone:function(t,n){this[t]=!0,n&&(this.active=n)}}},l=c,r=(e("e098"),e("2877")),m=Object(r["a"])(l,o,i,!1,null,"1c6afea8",null);n["default"]=m.exports},"4c62":function(t,n,e){},e098:function(t,n,e){"use strict";e("4c62")}}]);