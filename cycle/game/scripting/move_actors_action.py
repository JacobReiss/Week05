from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

class MoveActorsAction(Action):

    def __init__(self) -> None:
        super().__init__()

# Override the execute(cast, script) method as follows:
    def execute(self, cast, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
# 1) get all the actors from the cast
        actors = cast.get_all_actors()
# 2) loop through the actors
        for actor in actors: 
# 3) call the move_next() method on each actor
            actor.move_next()