class Task extends Spine.Model
  @configure "Task", "name", "done"
  
  #@extend Spine.Model.Local
  @extend Spine.Model.Ajax

  #@url: "/tasks/"

  @active: ->
    @select (item) -> !item.done

  @done: ->
    @select (item) -> !!item.done

  @destroyDone: ->
    rec.destroy() for rec in @done()

module.exports = Task