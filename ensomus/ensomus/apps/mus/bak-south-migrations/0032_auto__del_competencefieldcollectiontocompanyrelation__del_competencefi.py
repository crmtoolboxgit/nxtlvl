# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Deleting model 'CompetenceFieldCollectionToCompanyRelation'
        db.delete_table(u'mus_competencefieldcollectiontocompanyrelation')

        # Deleting model 'CompetenceFieldCollection'
        db.delete_table(u'mus_competencefieldcollection')

        # Deleting model 'CompetenceFieldCollectionToUserRelation'
        db.delete_table(u'mus_competencefieldcollectiontouserrelation')

        # Deleting model 'CompetenceFieldCollectionCompetenceField'
        db.delete_table(u'mus_competencefieldcollectioncompetencefield')

        # Adding model 'DevelopmentPlanToUserRelation'
        db.create_table(u'mus_developmentplantouserrelation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('finished_at', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='competence_field_collection_user_created_by', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'mus', ['DevelopmentPlanToUserRelation'])

        # Deleting field 'QuestionResponse.competence_field_collection_to_user_relation'
        db.delete_column(u'mus_questionresponse', 'competence_field_collection_to_user_relation_id')

        # Adding field 'QuestionResponse.development_plan_to_user_relation'
        db.add_column(u'mus_questionresponse', 'development_plan_to_user_relation',
                      self.gf('django.db.models.fields.related.ForeignKey')(
                          related_name='question_response_development_plan_to_user_relation',
                          to=orm['mus.DevelopmentPlanToUserRelation']),
                      keep_default=False)

        # Adding M2M table for field competence_fields on 'DevelopmentPlan'
        db.create_table(u'mus_developmentplan_competence_fields', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('developmentplan', models.ForeignKey(orm[u'mus.developmentplan'], null=False)),
            ('competencefield', models.ForeignKey(orm[u'mus.competencefield'], null=False))
        ))
        db.create_unique(u'mus_developmentplan_competence_fields', ['developmentplan_id', 'competencefield_id'])


        # Changing field 'DevelopmentPlan.manager_response_relation'
        db.alter_column(u'mus_developmentplan', 'manager_response_relation_id',
                        self.gf('django.db.models.fields.related.ForeignKey')(
                            to=orm['mus.DevelopmentPlanToUserRelation']))

        # Changing field 'DevelopmentPlan.employee_response_relation'
        db.alter_column(u'mus_developmentplan', 'employee_response_relation_id',
                        self.gf('django.db.models.fields.related.ForeignKey')(
                            to=orm['mus.DevelopmentPlanToUserRelation']))

    def backwards(self, orm):
        # Adding model 'CompetenceFieldCollectionToCompanyRelation'
        db.create_table(u'mus_competencefieldcollectiontocompanyrelation', (
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mus.Company'])),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='competence_field_collection_company_created_by', to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('competence_field_collection',
             self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mus.CompetenceFieldCollection'])),
        ))
        db.send_create_signal('mus', ['CompetenceFieldCollectionToCompanyRelation'])

        # Adding model 'CompetenceFieldCollection'
        db.create_table(u'mus_competencefieldcollection', (
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='competence_field_collection_updated_by', to=orm['auth.User'])),
            ('description', self.gf('tinymce.models.HTMLField')(null=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=4000)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='competence_field_collection_created_by', to=orm['auth.User'])),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('mus', ['CompetenceFieldCollection'])

        # Adding model 'CompetenceFieldCollectionToUserRelation'
        db.create_table(u'mus_competencefieldcollectiontouserrelation', (
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='competence_field_collection_user_created_by', to=orm['auth.User'])),
            ('finished_at', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('competence_field_collection', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parent',
                                                                                                  to=orm[
                                                                                                      'mus.CompetenceFieldCollection'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('mus', ['CompetenceFieldCollectionToUserRelation'])

        # Adding model 'CompetenceFieldCollectionCompetenceField'
        db.create_table(u'mus_competencefieldcollectioncompetencefield', (
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(
                related_name='competence_field_collection_competence_field_created_by', to=orm['auth.User'])),
            ('competence_field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mus.CompetenceField'])),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('competence_field_collection',
             self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mus.CompetenceFieldCollection'])),
        ))
        db.send_create_signal('mus', ['CompetenceFieldCollectionCompetenceField'])

        # Deleting model 'DevelopmentPlanToUserRelation'
        db.delete_table(u'mus_developmentplantouserrelation')

        # Adding field 'QuestionResponse.competence_field_collection_to_user_relation'
        db.add_column(u'mus_questionresponse', 'competence_field_collection_to_user_relation',
                      self.gf('django.db.models.fields.related.ForeignKey')(
                          related_name='question_response_competence_field_collection_to_user_relation',
                          to=orm['mus.CompetenceFieldCollectionToUserRelation']),
                      keep_default=False)

        # Deleting field 'QuestionResponse.development_plan_to_user_relation'
        db.delete_column(u'mus_questionresponse', 'development_plan_to_user_relation_id')

        # Removing M2M table for field competence_fields on 'DevelopmentPlan'
        db.delete_table('mus_developmentplan_competence_fields')


        # Changing field 'DevelopmentPlan.manager_response_relation'
        db.alter_column(u'mus_developmentplan', 'manager_response_relation_id',
                        self.gf('django.db.models.fields.related.ForeignKey')(
                            to=orm['mus.CompetenceFieldCollectionToUserRelation']))

        # Changing field 'DevelopmentPlan.employee_response_relation'
        db.alter_column(u'mus_developmentplan', 'employee_response_relation_id',
                        self.gf('django.db.models.fields.related.ForeignKey')(
                            to=orm['mus.CompetenceFieldCollectionToUserRelation']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [],
                            {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')",
                     'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': (
                'django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [],
                       {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True',
                        'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [],
                                 {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True',
                                  'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)",
                     'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mus.action': {
            'Meta': {'object_name': 'Action'},
            'action_key': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'actions'", 'to': u"orm['mus.ActionKey']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'action_created_by'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'action_updated_by'", 'to': u"orm['auth.User']"})
        },
        u'mus.actionkey': {
            'Meta': {'object_name': 'ActionKey'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'action_key_created_by'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'action_key_updated_by'", 'to': u"orm['auth.User']"})
        },
        u'mus.actionkeytodevelopmentplanrelation': {
            'Meta': {'object_name': 'ActionKeyToDevelopmentPlanRelation'},
            'action_key': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mus.ActionKey']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'development_plan_relation': ('django.db.models.fields.related.ForeignKey', [],
                                          {'related_name': "'action_key_to_development_plan_relation'",
                                           'to': u"orm['mus.DevelopmentPlan']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'mus.actionresponse': {
            'Meta': {'object_name': 'ActionResponse'},
            'action': ('django.db.models.fields.related.ForeignKey', [],
                       {'related_name': "'action_responses'", 'to': u"orm['mus.Action']"}),
            'action_key_to_development_plan_relation': ('django.db.models.fields.related.ForeignKey', [],
                                                        {'related_name': "'action_responses'",
                                                         'to': u"orm['mus.ActionKeyToDevelopmentPlanRelation']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'action_response_created_by'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'action_response_updated_by'", 'to': u"orm['auth.User']"})
        },
        u'mus.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'assignment_key': ('django.db.models.fields.related.ForeignKey', [],
                               {'related_name': "'assignments'", 'to': u"orm['mus.AssignmentKey']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'assignment_created_by'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('tinymce.models.HTMLField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'assignment_updated_by'", 'to': u"orm['auth.User']"})
        },
        u'mus.assignmentkey': {
            'Meta': {'object_name': 'AssignmentKey'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        u'mus.assignmentkeytouserrelation': {
            'Meta': {'object_name': 'AssignmentKeyToUserRelation'},
            'assignment_key': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mus.AssignmentKey']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'assignment_key_to_user_relation_created_by'", 'to': u"orm['auth.User']"}),
            'finished_at': (
                'django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'mus.assignmentresponse': {
            'Meta': {'object_name': 'AssignmentResponse'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'assignment_responses'", 'to': u"orm['mus.Assignment']"}),
            'assignment_key_to_user_relation': ('django.db.models.fields.related.ForeignKey', [],
                                                {'related_name': "'assignment_responses'",
                                                 'to': u"orm['mus.AssignmentKeyToUserRelation']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text_assignment': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'text_competence': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'mus.company': {
            'Meta': {'object_name': 'Company'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'company_created_by'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'company_updated_by'", 'to': u"orm['auth.User']"})
        },
        u'mus.competence': {
            'Meta': {'object_name': 'Competence'},
            'competence_field': ('django.db.models.fields.related.ForeignKey', [],
                                 {'related_name': "'competence_competence_field'",
                                  'to': u"orm['mus.CompetenceField']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'competence_created_by'", 'to': u"orm['auth.User']"}),
            'description': ('tinymce.models.HTMLField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'competence_updated_by'", 'to': u"orm['auth.User']"})
        },
        u'mus.competencefield': {
            'Meta': {'object_name': 'CompetenceField'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'competence_field_created_by'", 'to': u"orm['auth.User']"}),
            'description': ('tinymce.models.HTMLField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions': ('django.db.models.fields.related.ManyToManyField', [],
                          {'to': u"orm['mus.Question']", 'through': u"orm['mus.CompetenceQuestion']",
                           'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '4000'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'competence_field_updated_by'", 'to': u"orm['auth.User']"})
        },
        u'mus.competencequestion': {
            'Meta': {'object_name': 'CompetenceQuestion'},
            'competence_field': (
                'django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mus.CompetenceField']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'competence_question_created_by'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mus.Question']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'mus.developmentplan': {
            'Meta': {'object_name': 'DevelopmentPlan'},
            'competence_fields': ('django.db.models.fields.related.ManyToManyField', [],
                                  {'related_name': "'development_plan_competence_fields'", 'symmetrical': 'False',
                                   'to': u"orm['mus.CompetenceField']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'development_plan_created_by'", 'to': u"orm['auth.User']"}),
            'employee_assignment_key_relation': ('django.db.models.fields.related.ForeignKey', [],
                                                 {'related_name': "'development_plan_employee_assignment_key_relation'",
                                                  'to': u"orm['mus.AssignmentKeyToUserRelation']"}),
            'employee_response_relation': ('django.db.models.fields.related.ForeignKey', [],
                                           {'related_name': "'development_plan_employee'",
                                            'to': u"orm['mus.DevelopmentPlanToUserRelation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager_assignment_key_relation': ('django.db.models.fields.related.ForeignKey', [],
                                                {'related_name': "'development_plan_manager_assignment_key_relation'",
                                                 'to': u"orm['mus.AssignmentKeyToUserRelation']"}),
            'manager_response_relation': ('django.db.models.fields.related.ForeignKey', [],
                                          {'related_name': "'development_plan_manager'",
                                           'to': u"orm['mus.DevelopmentPlanToUserRelation']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mus.Employee']"})
        },
        u'mus.developmentplantouserrelation': {
            'Meta': {'object_name': 'DevelopmentPlanToUserRelation'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'competence_field_collection_user_created_by'",
                            'to': u"orm['auth.User']"}),
            'finished_at': (
                'django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'mus.employee': {
            'Meta': {'object_name': 'Employee'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mus.Company']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'employee_created_by'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manager': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manager': ('django.db.models.fields.related.ForeignKey', [],
                        {'to': u"orm['mus.Employee']", 'null': 'True', 'blank': 'True'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [],
                      {'to': u"orm['mus.Role']", 'through': u"orm['mus.EmployeeRole']", 'symmetrical': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'employee_updated_by'", 'to': u"orm['auth.User']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [],
                     {'related_name': "'employee_user'", 'to': u"orm['auth.User']"})
        },
        u'mus.employeerole': {
            'Meta': {'object_name': 'EmployeeRole'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'employee_role_created_by'", 'to': u"orm['auth.User']"}),
            'employee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mus.Employee']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mus.Role']"})
        },
        u'mus.file': {
            'Meta': {'object_name': 'File'},
            'company': (
                'django.db.models.fields.related.ForeignKey', [],
                {'related_name': "'files'", 'to': u"orm['mus.Company']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'file_created_by'", 'to': u"orm['auth.User']"}),
            'file': ('django.db.models.fields.related.ForeignKey', [],
                     {'default': 'None', 'to': u"orm['mus.FileBytes']", 'null': 'True', 'blank': 'True'}),
            'file_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'file_path': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'file_size': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mime_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'role': ('django.db.models.fields.related.ForeignKey', [],
                     {'default': 'None', 'related_name': "'files'", 'null': 'True', 'blank': 'True',
                      'to': u"orm['mus.Role']"})
        },
        u'mus.filebytes': {
            'Meta': {'object_name': 'FileBytes'},
            '_data': ('django.db.models.fields.TextField', [], {'db_column': "'data'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mus.question': {
            'Meta': {'object_name': 'Question'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'question_created_by'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('tinymce.models.HTMLField', [], {'max_length': '4000'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'question_updated_by'", 'to': u"orm['auth.User']"})
        },
        u'mus.questionresponse': {
            'Meta': {'object_name': 'QuestionResponse'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'question_response_created_by'", 'to': u"orm['auth.User']"}),
            'development_plan_to_user_relation': ('django.db.models.fields.related.ForeignKey', [], {
                'related_name': "'question_response_development_plan_to_user_relation'",
                'to': u"orm['mus.DevelopmentPlanToUserRelation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mus.Question']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'question_response_updated_by'", 'to': u"orm['auth.User']"})
        },
        u'mus.role': {
            'Meta': {'object_name': 'Role'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'role_created_by'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [],
                           {'related_name': "'role_updated_by'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['mus']