from app import db, models


class CmdOp:
    def add_new_cmd(self, form):
        cmd = models.RemoteCmd(cmd_name=form.remote_cmd_name.data, cmd=form.remote_cmd.data)
        db.session.add(cmd)
        db.session.commit()

    def show_all_cmds(self):
        cmds = models.RemoteCmd.query.all()
        return cmds

    def get_cmd_byid(self, cmd_id):
        cmd = models.RemoteCmd.query.filter_by(id=cmd_id).first()
        return cmd

    def delete_cmd_byid(self, cmd_id):
        cmd = models.RemoteCmd.query.filter_by(id=cmd_id).first()
        if cmd is not None:
            db.session.delete(cmd)
            db.session.commit()

