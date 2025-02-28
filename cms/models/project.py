from odoo import models, fields, _

class Cms(models.Model):
    _inherit = 'project.project'

    contract_name = fields.Char()

    # Contract Identification
    contract_id = fields.Char(string="Contract No", required=False, copy=False, index=False)
    contract_title = fields.Char(string="Contract Title", required=False)    
    
    award_type = fields.Many2one(
        comodel_name='award.type',
        string="Award Type",
        help="Select or create an Award Type."
    )
    
    contract_type = fields.Many2one(
        comodel_name='contract.type',
        string="Contract Type",
        help="Select or create a Contract Type."
    )


    # Parties Involved
    vendor_name = fields.Many2one('res.partner', string="Vendor/Supplier")
    vendor_contact = fields.Char(string="Vendor/Supplier Contact Information")
    company_representative_id = fields.Many2one('res.users', string="Our Company Representative")
    
    tags = fields.Many2many('tags.tags', string="Tags")
    
    # # Key Dates-*- coding: utf-8 -*-
    date_start = fields.Date(string="Contract Period(planned date)", required=False)
    start_date = fields.Date(string="Contract period (planned Date)", required=True)
    signing_date = fields.Date(string="Contract signing date", required=False)
    end_date = fields.Date(string="End Date")
    renewal_date = fields.Date(string="Renewal Date")
    termination_date = fields.Date(string="Termination Date")

    # # Financial Details
    contract_value = fields.Monetary(string="Contract Value", currency_field='currency_id')
    payment_terms = fields.Char(string="Payment Terms")
    currency_id = fields.Many2one('res.currency', string="Currency")
    penalty_clauses = fields.Char(string="Penalty Clauses")

    # # Scope of Work
    description_services = fields.Char(string="Description of Services/Goods")
    deliverables = fields.Char(string="Deliverables")

    # # Legal and Compliance
    governing_law = fields.Char(string="Governing Law")
    dispute_resolution = fields.Selection([
        ('arbitration', 'Arbitration'),
        ('mediation', 'Mediation'),
        ('litigation', 'Litigation')
    ], string="Dispute Resolution")
    confidentiality_clauses = fields.Char(string="Confidentiality Clauses")
    compliance_requirements = fields.Char(string="Compliance Requirements")

    # Status Tracking
    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('terminated', 'Terminated')
    ], string="Status", default='draft')
    approval_status = fields.Selection([
        ('pending', 'Pending Approval'),
        ('approved', 'Approved')
    ], string="Approval Status", default='pending')
    signed_date = fields.Date(string="Signed Date")
    signed_by = fields.Char(string="Signed By")

    # Management and Oversight
    contract_manager_id = fields.Many2one('res.users', string="Contract Manager")
    performance_metrics = fields.Char(string="Performance Metrics")
    risk_assessment = fields.Char(string="Risk Assessment")

    # Documents and Amendments
    attachment_ids = fields.Many2many('ir.attachment', string="Attachments")
    amendment_history = fields.Char(string="Amendment History")
    version_number = fields.Integer(string="Version Number")

    # Reporting and Analyticsheader
    category_id = fields.Many2one('project.category', string="Category")
    department_id = fields.Many2one('hr.department', string="Department")
    budget_code = fields.Char(string="Budget Code")
    cost_center = fields.Char(string="Cost Center")
    
    extension = fields.Many2one('cms.extension')
    payment = fields.Many2one('cms.payment')

    # Automation and Notifications
    notification_triggers = fields.Char(string="Notification Triggers")
    escalation_points = fields.Many2many('res.users', string="Escalation Points")
    
    
    approval_count = fields.Integer(
        string='Approvals', 
        compute='_compute_approval_count'
    )

    def _compute_approval_count(self):
        for project in self:
            project.approval_count = self.env['approval.request'].search_count([
                ('project_id', '=', project.id)  # Use the correct field name here
            ])

    def action_open_approvals(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Approvals',
            'res_model': 'approval.request',
            'view_mode': 'tree,form',
            'domain': [('project_id', '=', self.id)],  # Correct field name here
        }

