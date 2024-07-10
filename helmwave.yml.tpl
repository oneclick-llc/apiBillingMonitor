version: 0.36.4

registries:
- host: cr.yandex

repositories:  
- url: https://chart.onechart.dev
  name: onechart

.options: &options
  wait: true
  timeout: 5m
  create_namespace: true
  max_history: 3
  namespace: {{ requiredEnv "NAMESPACE" }}
  pending_release_strategy: rollback

releases:
  - name: apibillingmonitor
    tags:
    - apiBillingMonitor
    - prod
    <<: *options
    values:
    - src: helm/yc/{{ requiredEnv "VALUES_ENV" }}/values.yml
      strict: true
      delimiter_left: "[["
      delimiter_right: "]]"
    chart:
      name: onechart/cron-job
      version: 0.66.0