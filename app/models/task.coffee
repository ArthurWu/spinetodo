class Task extends Spine.Model
  @configure "Task", "name", "done"

  @extend Spine.Model.Local

  @active: ->
    @select (item) -> !item.done

  @done: ->
    @select (item) -> !!item.done

  @destroyDone: ->
    res.destroy() for res in @done

module.exports = Task