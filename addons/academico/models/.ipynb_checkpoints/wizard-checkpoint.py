from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'academico.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    session_id = fields.Many2one('academico.session',
        string="Session", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    
    def _default_session(self):
        return self.env['academico.session'].browse(self._context.get('active_id'))

    session_id = fields.Many2one('academico.session',
        string="Session", required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    def subscribe(self):
        self.session_id.attendee_ids |= self.attendee_ids
        return {}
    
    def _default_sessions(self):
        return self.env['academico.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many('academico.session',
        string="Sessions", required=True, default=_default_sessions)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
