from odoo import models, fields, api


class contractType(models.Model):
    _name = 'contract.type'
    _description = 'contract types for contract management system'
    _rec_name = 'contract_name' 

    contract_name = fields.Char(string="name")



class AwardType(models.Model):
    _name = 'award.type'
    _description = 'award types for contract management system'
    _rec_name = 'award_name'

    award_name = fields.Char(string="name")

class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    project_id = fields.Many2one(
        'project.project', 
        string="Project", 
        help="Linked project for this approval request"
    )


class Extension(models.Model):
    _name = 'cms.extension'
    
    
    extension_date = fields.Char(string="Extension Date")
    
    extension_reason = fields.Char(string="Extension Reason")
    
    New_end_date = fields.Char(string="New End Date")
    
    approved_by = fields.Char(string="Approved By")




class Payment(models.Model):
    _name = 'cms.payment'
    
    payment_date = fields.Char(string="Payment Date")
    
    amount = fields.Char(string="amount")
    
    approved_by = fields.Char(string="Approved by")
    

