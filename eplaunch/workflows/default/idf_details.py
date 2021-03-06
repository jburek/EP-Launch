import os

from eplaunch.workflows.base import BaseEPLaunchWorkflow1, EPLaunchWorkflowResponse1


class ColumnNames:
    Version = 'Version'
    NumDesignDays = '# Design Days'
    NumRunPeriods = '# Run Periods'
    NumZones = '# Zones'


class IDFDetailsWorkflow1(BaseEPLaunchWorkflow1):

    def name(self):
        return "IDF Details 1.0"

    def context(self):
        return "EPLaunch 2.9.2"

    def description(self):
        return "Retrieves IDF Details"

    def get_file_types(self):
        return ["*.idf"]

    def get_output_suffixes(self):
        return []

    def get_interface_columns(self):
        return [
            ColumnNames.Version,
            ColumnNames.NumDesignDays,
            ColumnNames.NumRunPeriods,
            ColumnNames.NumZones
        ]

    def main(self, run_directory, file_name, args):
        self.callback("In IDFDetailsWorkflow.main(), about to process file")
        file_path = os.path.join(run_directory, file_name)
        content = open(file_path).read()
        new_lines = []
        try:
            for line in content.split('\n'):
                if line.strip() == '':
                    continue
                if '!' not in line:
                    new_lines.append(line.strip())
                else:
                    line_without_comment = line[0:line.index('!')].strip()
                    if line_without_comment != '':
                        new_lines.append(line_without_comment)
        except Exception as e:
            self.callback("Could not process IDF; error: " + str(e))
            return EPLaunchWorkflowResponse1(
                success=False,
                message='Could not parse IDF object data!',
                column_data={
                    ColumnNames.Version: '*unknown*',
                    ColumnNames.NumDesignDays: '*unknown*',
                    ColumnNames.NumRunPeriods: '*unknown*',
                    ColumnNames.NumZones: '*unknown*'
                }
            )
        one_long_line = ''.join(new_lines)
        objects = one_long_line.split(';')
        num_dds = 0
        num_rps = 0
        num_zones = 0
        version_id = '*unknown*'
        for obj in objects:
            if obj.upper().startswith('SIZINGPERIOD:DESIGNDAY'):
                num_dds += 1
            elif obj.upper().startswith('RUNPERIOD'):
                num_rps += 1
            elif obj.upper().startswith('ZONE,'):
                num_zones += 1
            elif obj.upper().startswith('VERSION,'):
                version_fields = obj.split(',')
                version_id = version_fields[1]
        self.callback("Completed IDFDetailsWorkflow.main()")
        return EPLaunchWorkflowResponse1(
            success=True,
            message='Parsed IDF information successfully',
            column_data={
                ColumnNames.Version: version_id,
                ColumnNames.NumDesignDays: num_dds,
                ColumnNames.NumRunPeriods: num_rps,
                ColumnNames.NumZones: num_zones
            }
        )
