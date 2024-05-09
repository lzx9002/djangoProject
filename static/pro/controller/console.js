/**

 @Name：layuiAdmin 主页控制台
 @Author：贤心
 @Site：http://www.layui.com/admin/
 @License：LPPL
    
 */


layui.define(function(exports){
  
  /*
    下面通过 layui.use 分段加载不同的模块，实现不同区域的同时渲染，从而保证视图的快速呈现
  */

  const echartsOptions =
      {
          animation: false,
          title: {
              text: "服务器系统使用率",
              x: "center",
              textStyle: {
                  fontSize: 14
              }
          },
          tooltip: {
              trigger: "axis"
          },
          legend: {
              data: [
                  "",
                  ""
              ]
          },
          xAxis: [
              {
                  type: "category",
                  boundaryGap: false,
                  data: []
              }
          ],
          yAxis: [
              {
                  type: "value"
              }
          ],
          series: [
              {
                  name: "cpu",
                  type: "line",
                  smooth: true,
                  itemStyle: {
                      normal: {
                          areaStyle: {
                              type: "default"
                          }
                      }
                  },
                  data: []
              },
              {
                  name: "memory",
                  type: "line",
                  smooth: true,
                  itemStyle: {
                      normal: {
                          areaStyle: {
                              type: "default"
                          }
                      }
                  },
                  data: []
              }
          ]
      };

  //数据概览
  layui.use(['admin', 'carousel', 'echarts'], function(){
    let $ = layui.$
        , admin = layui.admin
        , carousel = layui.carousel
        , echarts = layui.echarts;

    const $dataview = $('#LAY-index-dataview')
    const sign = new Date().getTime();
    $dataview.data('sign', sign);

    var echartsApp = null;
    function loadHistory() {
      admin.req({
        url: '/api/CPUUsageOverview/',
        done: function (res) {

          const data = res.data;
          const options = echartsOptions;
          options.xAxis[0].data = data.time;
          options.series[0].data = data.cpu;
          options.series[1].data = data.memory;

          function renderDataView(index) {

            echartsApp = echarts.init($dataview[0], layui.echartsTheme);
            echartsApp.setOption(options);

            //
            admin.resize(function () {
              echartsApp[index].resize();
            });

            //监听侧边伸缩
            layui.admin.on('side', function(){
              echartsApp = null;
            });

            //监听路由
            layui.admin.on('hash(tab)', function(){
              const url = layui.router().path.join('') ;
              if (url) echartsApp = null; //|| renderDataView(carouselIndex);
            });
          }

          if (!echartsApp) {
            renderDataView();
          }  else {
            // echartsApp.clear();
            echartsApp.setOption(options);
          }
          const sign2 = $dataview.data('sign');
          if (sign2 === sign) {
            setTimeout(() => {
              loadHistory(sign)
            }, 10000)
          }
        }
      });
    }
    loadHistory(sign);
  });
  layui.use(['admin', 'carousel', 'echarts', 'laytpl'], function(){
    let $ = layui.$,
        admin = layui.admin,
        carousel = layui.carousel,
        echarts = layui.echarts,
        element = layui.element,
        laytpl = layui.laytpl;

    const sign = new Date().getTime();
     $("[lay-filter='cpu-progress'] .layui-progress-bar").data('sign', sign);
    function refresh(sign) {
      admin.req({
        url: '/api/cpuMemoryInfo/'
        ,done: function(res) {

            let Info = {
              ram: $("[lay-filter='ram-progress'] .layui-progress-bar"),
              ramText: $("[layui-filter='ram-progress'] .layui-progress-text"),
              cpu: $("[lay-filter='cpu-progress'] .layui-progress-bar"),
              cpuText: $("[layui-filter='cpu-progress'] .layui-progress-text"),
              memUsage: $("#MemoryUsageValues"),
              templCpu: $('#templ-cpu'),
              cpus: $('#cpus'),
            };

          if (res.data.cpu > 80) {
            Info['cpu'].addClass('layui-bg-red');
          } else {
            Info['cpu'].removeClass('layui-bg-red');
          }

          if (res.data.memory > 80) {
            Info['ram'].addClass('layui-bg-red');
          } else {
            Info['ram'].removeClass('layui-bg-red');
          }
          element.progress('cpu-progress', res.data.cpu + '%')
          Info['cpuText'].text(res.data.cpu + '%')
          element.progress('ram-progress', res.data.memory + '%')
          Info['ramText'].text(res.data.memory + '%')

          Info['memUsage'].html(res.data.MemoryUsageRate + '/' + res.data.TotalMemory)

          // render cpus
          // const templ = Info[5].html();
          const templ = '\
          {{# layui.each(d, function(index, item) { }}\
            <div class="layui-col-xs12 layui-col-sm6 layui-col-md6">\
              <div class="layui-card">\
                <div class="layui-card-header">cpu核心{{index+1}}</div>\
                <div class="layui-card-body layadmin-takerates">\
                  <div id="cpu1" class="layui-progress" lay-showPercent="yes" lay-filter="cpu1-progress">\
                    <h3>cpu核心{{index+1}}占用率</h3>\
                    <div class="layui-progress-bar" lay-percent="{{item}}%">\
                      <span class="layui-progress-text" lay-filter="cpu1-progress">{{item}}%</span>\
                    </div>\
                  </div>\
                </div>\
              </div>\
            </div>\
          {{# }) }}';
          const str = laytpl(templ).render(res.data.cpu_count);
          // layui.each(res.data.cpu_count, function (index, item) {
          //   const str = laytpl(templ).render({index: index, item: item});
          //   Info[6].html(str)
          // })
          Info['cpus'].html(str)


          const sign2 = Info['cpu'].data('sign');
          if (sign2 === sign) {
            setTimeout(() => {
              refresh(sign)
            }, 500)
          }
        }
      });
    }

    refresh(sign);
  });
  exports('console', {})
});